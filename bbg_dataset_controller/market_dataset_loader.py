from .path_director import file_folder
from .bbg_dataset_utils import FILENAME_SECTOR_NAME
from shining_pebbles import scan_files_including_regex, open_df_in_file_folder_by_regex

def open_df_name_sector_of_bbg_index(ticker_bbg_index, date_ref=None):
    regex = FILENAME_SECTOR_NAME(ticker_bbg_index) if date_ref is None else FILENAME_SECTOR_NAME(ticker_bbg_index, date_ref)
    file_name = scan_files_including_regex(file_folder=file_folder['market'], regex=regex)[-1]
    df = open_df_in_file_folder_by_regex(file_folder=file_folder['market'], regex=file_name)
    return df
