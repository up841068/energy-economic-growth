import sys
sys.path.insert(0, '..')
sys.path.insert(0, '../..')

import numpy as np
import pandas as pd

from pathlib import Path
from colorama import Fore, Style

from energy_economy.ml_logic.data import get_data_with_cache
from energy_economy.ml_logic.registry import load_model, save_model, mlflow_transition_model
from energy_economy.ml_logic.model import initialize_model, train_model, evaluate_model
from sklearn.metrics import r2_score
from energy_economy.params import *
from pathlib import Path

#OK!
def train() -> None:
    """
    - Download processed train/test data from your BQ table (or from cache if it exists). #OK!!
    - Cache query result as a local CSV if it doesn't exist locally. #OK!!
    - Train on the preprocessed dataset. #OK!!
    - Store training results. #OK!!

    Return model r2 score as a float. #OK!
    """

    print(Fore.MAGENTA + "\n⭐️ Use case: train" + Style.RESET_ALL)
    print(Fore.BLUE + "\nLoading preprocessed validation data..." + Style.RESET_ALL)

    # Load processed data using `get_data_with_cache`
    # Query the preprocessed dataset from Energy-Economy's BigQuery dataset
    query_train = f"""
        SELECT {",".join(COLUMN_NAMES)}
        FROM {GCP_PROJECT}.{BQ_DATASET}.{GCP_TABLE_TRAIN}
        """

    # Path to check if df is saved locally
    data_processed_cache_path_train = Path(LOCAL_DATA_PATH).joinpath("train", "full_cleaned_final_train.csv")

    # Function that loads df from BigQuery or locally, and saves if does not exist locally
    df_train = get_data_with_cache(gcp_project=GCP_PROJECT,
                            query=query_train,
                            cache_path=data_processed_cache_path_train,
                            data_has_header=True)

    # Create (X_train, y_train)
    X_train = df_train[['scale__coal_elec_per_capita',
                        'scale__oil_elec_per_capita',
                        'scale__gas_elec_per_capita',
                        'scale__hydro_elec_per_capita',
                        'scale__nuclear_elec_per_capita',
                        'scale__biofuel_elec_per_capita',
                        'scale__solar_elec_per_capita',
                        'scale__wind_elec_per_capita']]

    y_train = df_train['remainder__GDP_per_capita']

    # Loads model in production stage if it already exists
    model = load_model()

    # Verifies if the model already exists, and if it doesn't, initialize a new one
    if model is None:
        model = initialize_model()

    # Train model using `model.py`
    model = train_model(model,
                        X_train,
                        y_train)

    # Get the r2 score of the training dataset
    y_train_pred = model.predict(X_train)
    train_score = r2_score(y_train, y_train_pred)

    # Save model weight on the hard drive (and optionally on mlflow too!)
    save_model(model=model)

    # The latest model should be moved to staging
    # $CHA_BEGIN
    if MODEL_TARGET == 'mlflow':
        mlflow_transition_model(current_stage="None", new_stage="Staging")
    # $CHA_END

    print(f"✅ train() done: R2 score of {train_score} \n")

    return train_score

#OK!
def evaluate(stage: str = "Production") -> float:
    """
    Evaluate the performance of the latest production model on processed data #OK!
    Return model r2 score as a float #OK!
    """

    print(Fore.MAGENTA + "\n⭐️ Use case: evaluate" + Style.RESET_ALL)

    # Load the model
    model = load_model(stage=stage)
    assert model is not None

    # Load processed data using `get_data_with_cache`
    # Query the preprocessed dataset from Energy-Economy's BigQuery dataset
    query_test = f"""
        SELECT {",".join(COLUMN_NAMES)}
        FROM {GCP_PROJECT}.{BQ_DATASET}.{GCP_TABLE_TEST}
        """

    # Path to check if df is saved locally
    data_processed_cache_path_test = Path(LOCAL_DATA_PATH).joinpath("test", "full_cleaned_final_test.csv")

    # Function that loads df from BigQuery or locally, and saves locally if it does not exist
    df_test = get_data_with_cache(gcp_project=GCP_PROJECT,
                            query=query_test,
                            cache_path=data_processed_cache_path_test,
                            data_has_header=True)

    # Create (X_test, y_test)
    X_test = df_test[['scale__coal_elec_per_capita',
                        'scale__oil_elec_per_capita',
                        'scale__gas_elec_per_capita',
                        'scale__hydro_elec_per_capita',
                        'scale__nuclear_elec_per_capita',
                        'scale__biofuel_elec_per_capita',
                        'scale__solar_elec_per_capita',
                        'scale__wind_elec_per_capita']]

    y_test = df_test['remainder__GDP_per_capita']

    test_score = evaluate_model(model=model, X=X_test, y=y_test)

    print("✅ evaluate() done \n")

    return test_score


def pred(X_pred: pd.DataFrame = None) -> np.ndarray:
    """
    Make a prediction using the latest trained model
    """

    print("\n⭐️ Use case: predict")

    if X_pred is None:
        print("\nPlease insert some data, this model is hungry for inputs!!")

    # ADD A FUNCTION HERE THAT CONVERTS PERCENTAGE INPUT INTO ABSOLUTE VALUES TO BE USED AS INPUT TO THE PREDICTION
    # ADD A FUNCTION HERE THAT SCALES THE X_PRED USING THE PICKLE FILE
    model = load_model()
    assert model is not None

    y_pred = model.predict(X_pred)

    print("\n✅ prediction done: ", y_pred, y_pred.shape, "\n")

    return {'result': y_pred}


if __name__ == '__main__':
    X_pred = np.array([0.304435, 0.003186, 0.006744, 0.040087, 0.323919, 0.02055, 0, 0]).reshape(1, -1)
    train()
    evaluate()
    pred(X_pred)
