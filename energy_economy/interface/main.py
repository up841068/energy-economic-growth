import numpy as np
import pandas as pd

from pathlib import Path
from colorama import Fore, Style

from energy_economy.ml_logic.data import get_data_with_cache
from energy_economy.ml_logic.registry import load_model, save_model, mlflow_transition_model
from energy_economy.ml_logic.model import initialize_model, train_model, evaluate_model]
from sklearn.metrics import r2_score
from energy_economy.params import *
from pathlib import Path

def train() -> None:
    """
    - Query the processed train/test tables from Energy-Economy's BigQuery dataset (or from cache if it exists) #OK!!
    - Cache query result as a local CSV if it doesn't exist locally #OK!!
    - Train on the preprocessed dataset #OK!!
    - Store training results and model weights #OK!!

    Return model score as a float
    """


    # Query the preprocessed dataset from Energy-Economy's BigQuery dataset
    # Cache query result as a local CSV if it doesn't exist locally
    query_train = f"""
        SELECT {",".join(COLUMN_NAMES)}
        FROM {GCP_PROJECT}.{BQ_DATASET}.{GCP_TABLE_TRAIN}
        """

    query_test = f"""
        SELECT {",".join(COLUMN_NAMES)}
        FROM {GCP_PROJECT}.{BQ_DATASET}.{GCP_TABLE_TEST}
        """


    data_query_cache_path_train = Path(LOCAL_DATA_PATH).joinpath("train", "full_cleaned_final_train.csv")
    data_query_cache_path_test = Path(LOCAL_DATA_PATH).joinpath("test", "full_cleaned_final_test.csv")


    df_train = get_data_with_cache(gcp_project=GCP_PROJECT,
                            query=query_train,
                            cache_path=data_query_cache_path_train,
                            data_has_header=True)

    df_test = get_data_with_cache(gcp_project=GCP_PROJECT,
                            query=query_test,
                            cache_path=data_query_cache_path_test,
                            data_has_header=True)

    # Create (X_train_processed, y_train)
    X_train = df_train[['scale__coal_elec_per_capita',
                        'scale__oil_elec_per_capita',
                        'scale__gas_elec_per_capita',
                        'scale__hydro_elec_per_capita',
                        'scale__nuclear_elec_per_capita',
                        'scale__biofuel_elec_per_capita',
                        'scale__solar_elec_per_capita',
                        'scale__wind_elec_per_capita']]

    y_train = df_train['remainder__GDP_per_capita']

    # Train model using `model.py`
    model = load_model()

    # Verifies if the model already exists, and if it doesn't, initialize a new one
    if model is None:
        model = initialize_model()


    model = train_model(model,
                        X_train,
                        y_train)


    # Get the r2 score of the training dataset
    y_train_pred = model.predict(X_train)
    train_score = r2_score(y_train, y_train_pred)

    # Save model weight on the hard drive (and optionally on GCS too!)
    save_model(model=model)

    # The latest model should be moved to staging
    # $CHA_BEGIN
    if MODEL_TARGET == 'mlflow':
        mlflow_transition_model(current_stage="None", new_stage="Staging")
    # $CHA_END

    print("✅ train() done \n")

    return train_score



if __name__ == '__main__':
    train()
    evaluate_model()
    # pred()
