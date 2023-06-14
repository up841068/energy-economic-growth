from fastapi import FastAPI
import joblib
from energy_economy.params import *
from colorama import Fore, Style
import mlflow
from mlflow.tracking import MlflowClient
import pandas as pd


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

def predict(scale__coal_elec_per_capita,
            scale__oil_elec_per_capita,
            scale__gas_elec_per_capita,
            scale__hydro_elec_per_capita,
            scale__nuclear_elec_per_capita,
            scale__biofuel_elec_per_capita,
            scale__solar_elec_per_capita,
            scale__wind_elec_per_capita):
    # REMEMBER that the parameters passed above are of type str. So don't
    # forget to consider this and convert to numerical datatype (as below).

    # Loading the latest version of the model
    # model = load_model()
    model = joblib.load('20230614-155715.h5') # Loads local model

    # ADD A FUNCTION HERE THAT CONVERTS PERCENTAGE INPUT INTO ABSOLUTE VALUES TO BE USED AS INPUT TO THE PREDICTION

    X_pred = pd.DataFrame([scale__coal_elec_per_capita,
            scale__oil_elec_per_capita,
            scale__gas_elec_per_capita,
            scale__hydro_elec_per_capita,
            scale__nuclear_elec_per_capita,
            scale__biofuel_elec_per_capita,
            scale__solar_elec_per_capita,
            scale__wind_elec_per_capita], columns=['scale__coal_elec_per_capita',
                                                    'scale__oil_elec_per_capita',
                                                    'scale__gas_elec_per_capita',
                                                    'scale__hydro_elec_per_capita',
                                                    'scale__nuclear_elec_per_capita',
                                                    'scale__biofuel_elec_per_capita',
                                                    'scale__solar_elec_per_capita',
                                                    'scale__wind_elec_per_capita'])
    # Using the pickle file containing the fitted scaler to process the X_pred
    pipeline = joblib.load('prec.pkl')

    X_transformed = pipeline.transform(X_pred)
    result = model.predict(X_transformed)
    return {'result': result}

# preprocessar o input do usuario!!
