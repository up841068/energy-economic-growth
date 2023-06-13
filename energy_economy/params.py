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

COLUMN_NAMES_RAW_ENERGY = ['country', 'year', 'iso_code', 'net_elec_imports', 'per_capita_electricity','biofuel_elec_per_capita','hydro_elec_per_capita', 'solar_elec_per_capita','wind_elec_per_capita']
COLUMN_NAMES_RAW_GDP = ['Series Name', 'Series Code', 'Country Name', 'Country Code',
       '1990 [YR1990]', '2000 [YR2000]', '2013 [YR2013]', '2014 [YR2014]',
       '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]',
       '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]', '2022 [YR2022]',
       '2012 [YR2012]', '2011 [YR2011]', '2010 [YR2010]', '2009 [YR2009]',
       '2008 [YR2008]', '2007 [YR2007]', '2006 [YR2006]', '2005 [YR2005]',
       '2004 [YR2004]', '2003 [YR2003]', '2002 [YR2002]', '2001 [YR2001]',
       '1999 [YR1999]', '1998 [YR1998]', '1997 [YR1997]', '1996 [YR1996]',
       '1995 [YR1995]', '1994 [YR1994]', '1993 [YR1993]', '1992 [YR1992]',
       '1991 [YR1991]', '1989 [YR1989]', '1988 [YR1988]', '1987 [YR1987]',
       '1986 [YR1986]', '1985 [YR1985]', '1984 [YR1984]', '1983 [YR1983]',
       '1982 [YR1982]', '1981 [YR1981]', '1980 [YR1980]', '1979 [YR1979]',
       '1978 [YR1978]', '1977 [YR1977]', '1976 [YR1976]', '1975 [YR1975]',
       '1974 [YR1974]', '1973 [YR1973]', '1972 [YR1972]', '1971 [YR1971]',
       '1970 [YR1970]', '1969 [YR1969]', '1968 [YR1968]', '1967 [YR1967]',
       '1966 [YR1966]', '1965 [YR1965]', '1964 [YR1964]', '1963 [YR1963]',
       '1962 [YR1962]', '1961 [YR1961]', '1960 [YR1960]']

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
