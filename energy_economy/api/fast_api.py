import sys
sys.path.insert(0, '..')
sys.path.insert(0, '../..')

from fastapi import FastAPI
import joblib
from energy_economy.params import *
from colorama import Fore, Style
import mlflow
from mlflow.tracking import MlflowClient
import pandas as pd
import os

app = FastAPI()

# define a root '/' endpoint


def load_model(stage="Production"):
    """
    Return a saved model:
    - locally (latest one in alphabetical order)
    - or from GCS (most recent one) if MODEL_TARGET=='gcs'  --> for unit 02 only
    - or from MLFLOW (by "stage") if MODEL_TARGET=='mlflow' --> for unit 03 only #THIS ONE

    Return None (but do not Raise) if no model is found

    """

    if MODEL_TARGET == "mlflow":
        print(Fore.BLUE + f"\nLoad [{stage}] model from MLflow..." + Style.RESET_ALL)

        # Load model from MLflow
        model = None
        # $CHA_BEGIN
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        client = MlflowClient()

        try:
            model_versions = client.get_latest_versions(name=MLFLOW_MODEL_NAME, stages=[stage])
            model_uri = model_versions[0].source

            assert model_uri is not None
        except:
            print(f"\n❌ No model found with name {MLFLOW_MODEL_NAME} in stage {stage}")

            return None

        model = mlflow.tensorflow.load_model(model_uri=model_uri)

        print("✅ Model loaded from MLflow")
        # $CHA_END
        return model
    else:
        return None

# Each one of the below is an endpoint!
@app.get("/")
def index():
    # Here you can load a machine learning model
    # You can also do a prediction model.predict(...)
    return {'ok': True}


@app.get("/predict")

# what if you want to pass parameters to the endpoint?
# You just need to define the parameters you want to pass as
# the function parameters

def predict(coal_elec_per_capita,
            oil_elec_per_capita,
            gas_elec_per_capita,
            hydro_elec_per_capita,
            nuclear_elec_per_capita,
            biofuel_elec_per_capita,
            solar_elec_per_capita,
            wind_elec_per_capita):
    # REMEMBER that the parameters passed above are of type str. So don't
    # forget to consider this and convert to numerical datatype (as below).

    # Loading the latest version of the model
    # model = load_model()

    model = joblib.load('energy_economy/api/20230615-114031.h5') # Loads local model

    abs_energy_production = 7704

    X_pred = pd.DataFrame([[float(coal_elec_per_capita)*abs_energy_production,
            float(oil_elec_per_capita)*abs_energy_production,
            float(gas_elec_per_capita)*abs_energy_production,
            float(hydro_elec_per_capita)*abs_energy_production,
            float(nuclear_elec_per_capita)*abs_energy_production,
            float(biofuel_elec_per_capita)*abs_energy_production,
            float(solar_elec_per_capita)*abs_energy_production,
            float(wind_elec_per_capita)*abs_energy_production,
            str('Brazil'),
            int(2022),
            float(2000.09)]], columns=['coal_elec_per_capita',
                                        'oil_elec_per_capita',
                                        'gas_elec_per_capita',
                                        'hydro_elec_per_capita',
                                        'nuclear_elec_per_capita',
                                        'biofuel_elec_per_capita',
                                        'solar_elec_per_capita',
                                        'wind_elec_per_capita',
                                        'country',
                                        'year',
                                        'GDP_per_capita'])

    # Ordering the column names
    X_pred = X_pred[['country', 'year', 'coal_elec_per_capita', 'oil_elec_per_capita',
                    'gas_elec_per_capita', 'hydro_elec_per_capita',
                    'nuclear_elec_per_capita', 'biofuel_elec_per_capita',
                    'solar_elec_per_capita', 'wind_elec_per_capita', 'GDP_per_capita']]

    # Using the pickle file containing the fitted scaler to process the X_pred
    pipeline_scaler = joblib.load('energy_economy/api/prec.pkl')

    # Scaling the X_pred
    X_scaled = pd.DataFrame(pipeline_scaler.transform(X_pred),
                            columns=pipeline_scaler.get_feature_names_out())

    # Dropping the columns that are not used in the prediction
    X_scaled.drop(columns=['remainder__country', 'remainder__year', 'remainder__GDP_per_capita'], inplace=True)

    # Predicting the results with the X_scaled
    result = model.predict(X_scaled)
    return {'result': result[0]}


print(predict(coal_elec_per_capita=0.2,
            oil_elec_per_capita=0.2,
            gas_elec_per_capita=0.2,
            hydro_elec_per_capita=0.1,
            nuclear_elec_per_capita=0.1,
            biofuel_elec_per_capita=0.1,
            solar_elec_per_capita=0.05,
            wind_elec_per_capita=0.05))
