import numpy as np
import pandas as pd

from pathlib import Path
from colorama import Fore, Style
from dateutil.parser import parse

from energy_economy.ml_logic.data import get_data_with_cache
from energy_economy.params import *
from pathlib import Path

def preprocess() -> None:
    """
    - Query the raw dataset from Energy-Economy's BigQuery dataset #OK!!
    - Cache query result as a local CSV if it doesn't exist locally #OK!!
    - Process query data
    - Store processed data on your personal BQ (truncate existing table if it exists)
    - No need to cache processed data as CSV (it will be cached when queried back from BQ during training)
    """
    # Query the raw dataset from Energy-Economy's BigQuery dataset
    # Cache query result as a local CSV if it doesn't exist locally
    query_energy = f"""
        SELECT {",".join(COLUMN_NAMES_RAW_ENERGY)}
        FROM {GCP_PROJECT}.{BQ_DATASET}.{GCP_TABLE_ENERGY}
        ORDER BY country
        """

    query_gdp = f"""
        SELECT {",".join(COLUMN_NAMES_RAW_GDP)}
        FROM {GCP_PROJECT}.{BQ_DATASET}.{GCP_TABLE_ECONOMIC}
        """


    data_query_cache_path_energy = Path(LOCAL_DATA_PATH).joinpath("energy", "renewable_energy_data_scrapping.csv")
    data_query_cache_path_gdp = Path(LOCAL_DATA_PATH).joinpath("gdp", "World_Development_Indicators.csv")


    df_energy = get_data_with_cache(gcp_project=GCP_PROJECT,
                            query=query_energy,
                            cache_path=data_query_cache_path_energy,
                            data_has_header=True)

    df_gdp = get_data_with_cache(gcp_project=GCP_PROJECT,
                            query=query_gdp,
                            cache_path=data_query_cache_path_gdp,
                            data_has_header=True)

    return df_energy, df_gdp

df_energy, df_gdp = preprocess()

print(df_energy.head())
print(df_gdp.head())
