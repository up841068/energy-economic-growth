import numpy as np
import pandas as pd

from pathlib import Path
from colorama import Fore, Style
from dateutil.parser import parse

from data import get_data_with_cache
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
    query = f"""
        SELECT {",".join(COLUMN_NAMES_RAW)}
        FROM {GCP_PROJECT}.{BQ_DATASET}.{GCP_TABLE_ENERGY}
        ORDER BY country
        """


    data_query_cache_path = Path(LOCAL_DATA_PATH).joinpath("renewable-energy-data-scrapping.csv")
    df = get_data_with_cache(gcp_project=GCP_PROJECT,
                            query=query,
                            cache_path=data_query_cache_path,
                            data_has_header=True)
