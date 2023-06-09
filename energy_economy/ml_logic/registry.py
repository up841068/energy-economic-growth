import glob
import os
import time
import pickle
import joblib

from colorama import Fore, Style

from energy_economy.params import *
import mlflow
from mlflow.tracking import MlflowClient

#OK!
def save_model(model) -> None:
    """
    Persist trained model locally on the hard drive at f"{LOCAL_REGISTRY_PATH}/models/{timestamp}.h5" #OK!
    - if MODEL_TARGET='mlflow', also persist it on MLflow instead of GCS (for unit 0703 only) --> unit 03 only #OK!
    """

    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Save model locally
    model_path = os.path.join(LOCAL_REGISTRY_PATH, "models", f"{timestamp}.h5")
    joblib.dump(model, model_path)

    # Tries to save the model in mlflow
    if MODEL_TARGET == "mlflow":
        mlflow.tensorflow.log_model(
            model=model,
            artifact_path="model",
            registered_model_name=MLFLOW_MODEL_NAME)
        print("✅ Model saved to MLflow")

        return None
        # $CHA_END

    return None

#OK!
def load_model(stage="Production"):
    """
    Return a saved model: #OK!
    - locally (latest one in alphabetical order) #OK!
    - or from MLFLOW (by "stage") if MODEL_TARGET=='mlflow' --> for unit 05 only #OK!

    Return None (but do not Raise) if no model is found #OK!
    """

    if MODEL_TARGET == "local":
        print(Fore.BLUE + f"\nLoad latest model from local registry..." + Style.RESET_ALL)

        # Get the latest model version name by the timestamp on disk
        local_model_directory = os.path.join(LOCAL_REGISTRY_PATH, "models")
        local_model_paths = glob.glob(f"{local_model_directory}/*")

        if not local_model_paths:
            return None

        most_recent_model_path_on_disk = sorted(local_model_paths)[-1]

        print(Fore.BLUE + f"\nLoad latest model from disk..." + Style.RESET_ALL)

        latest_model = joblib.load(most_recent_model_path_on_disk)

        print("✅ Model loaded from local disk")

        return latest_model


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

#OK!
def mlflow_transition_model(current_stage: str, new_stage: str) -> None:
    """
    Transition the latest model from the `current_stage` to the. #OK!
    `new_stage` and archive the existing model in `new_stage`. #OK!
    """

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

    client = MlflowClient()

    version = client.get_latest_versions(name=MLFLOW_MODEL_NAME, stages=[current_stage])

    if not version:
        print(f"\n❌ No model found with name {MLFLOW_MODEL_NAME} in stage {current_stage}")
        return None

    client.transition_model_version_stage(
        name=MLFLOW_MODEL_NAME,
        version=version[0].version,
        stage=new_stage,
        archive_existing_versions=True)

    print(f"✅ Model {MLFLOW_MODEL_NAME} (version {version[0].version}) transitioned from {current_stage} to {new_stage}")

    return None


def mlflow_run(func):
    """
    Generic function to log params and results to MLflow along with TensorFlow auto-logging

    Args:
        - func (function): Function you want to run within the MLflow run
        - params (dict, optional): Params to add to the run in MLflow. Defaults to None.
        - context (str, optional): Param describing the context of the run. Defaults to "Train".
    """

    def wrapper(*args, **kwargs):
        mlflow.end_run()
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        mlflow.set_experiment(experiment_name=MLFLOW_EXPERIMENT)

        with mlflow.start_run():
            mlflow.tensorflow.autolog()
            results = func(*args, **kwargs)

        print("✅ mlflow_run auto-log done")

        return results
    return wrapper
