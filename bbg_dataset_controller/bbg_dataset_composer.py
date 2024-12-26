from .bbg_dataset_utils import FILENAME_SECTOR_NAME
from .bbg_dataset_loader import open_df_name_of_bbg_index, open_df_sector_of_bbg_index
from .path_director import file_folder
from .market_dataset_loader import open_df_name_sector_of_bbg_index
import pandas as pd
from shining_pebbles import get_today
from canonical_transformer import map_df_to_csv

def compose_df_name_sector_of_bbg_index(ticker_bbg_index):
    names = open_df_name_of_bbg_index(ticker_bbg_index=ticker_bbg_index)
    sectors = open_df_sector_of_bbg_index(ticker_bbg_index=ticker_bbg_index)
    name_sector = names.merge(sectors, how='outer', left_index=True, right_index=True)
    name_sector['ticker_bbg_index'] = ticker_bbg_index
    file_name = FILENAME_SECTOR_NAME(ticker_bbg_index)
    map_df_to_csv(df=name_sector, file_folder=file_folder['market'], file_name=file_name, include_index=True)
    return name_sector

def compose_df_ks_name_sector():
    df_kospi = open_df_name_sector_of_bbg_index(ticker_bbg_index='KOSPI Index')
    df_kosdaq = open_df_name_sector_of_bbg_index(ticker_bbg_index='KOSDAQ Index')
    df_ks = pd.concat([df_kospi, df_kosdaq])
    file_name = FILENAME_SECTOR_NAME('KS')
    file_name_alt = f'dataset-ks_name_sector-at{get_today("%Y%m%d")}-save{get_today("%Y%m%d")}.csv'
    map_df_to_csv(df=df_ks, file_folder=file_folder['market'], file_name=file_name, include_index=True)
    map_df_to_csv(df=df_ks, file_folder=file_folder['market'], file_name=file_name_alt, include_index=True)
    return df_ks