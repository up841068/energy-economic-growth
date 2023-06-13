import os
import numpy as np

##################  VARIABLES  ##################
GCP_PROJECT = os.environ.get("GCP_PROJECT") # OK
GCP_REGION = os.environ.get("GCP_REGION") # OK
BQ_DATASET = os.environ.get("BQ_DATASET") # OK
BQ_REGION = os.environ.get("BQ_REGION") # OK
BUCKET_NAME = os.environ.get("BUCKET_NAME") # OK
GCP_TABLE_ECONOMIC = os.environ.get("GCP_TABLE_ECONOMIC") # OK
GCP_TABLE_ENERGY = os.environ.get("GCP_TABLE_ENERGY") # OK


##################  CONSTANTS  #####################
LOCAL_DATA_PATH = os.path.join(os.path.expanduser('~'), ".lewagon", "mlops", "data", "raw") # OK
LOCAL_REGISTRY_PATH =  os.path.join(os.path.expanduser('~'), ".lewagon", "mlops", "training_outputs")

COLUMN_NAMES_RAW = ['country', 'year', 'iso_code', 'net_elec_imports', 'per_capita_electricity','biofuel_elec_per_capita','hydro_elec_per_capita', 'solar_elec_per_capita','wind_elec_per_capita']

# DTYPES_RAW = {
#     "fare_amount": "float32",
#     "pickup_datetime": "datetime64[ns, UTC]",
#     "pickup_longitude": "float32",
#     "pickup_latitude": "float32",
#     "dropoff_longitude": "float32",
#     "dropoff_latitude": "float32",
#     "passenger_count": "int16"
# }



################## VALIDATIONS #################

# env_valid_options = dict(
#     DATA_SIZE=["1k", "200k", "all"],
#     MODEL_TARGET=["local", "gcs", "mlflow"],
# )

# def validate_env_value(env, valid_options):
#     env_value = os.environ[env]
#     if env_value not in valid_options:
#         raise NameError(f"Invalid value for {env} in `.env` file: {env_value} must be in {valid_options}")


# for env, valid_options in env_valid_options.items():
#     validate_env_value(env, valid_options)
