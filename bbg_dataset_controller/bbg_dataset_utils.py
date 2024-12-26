from shining_pebbles import get_today

def format_filename_of_name_sector(ticker_bbg_index, date_ref=None):
    date_ref =(date_ref if date_ref else get_today("%Y%m%d")).replace('-', '')
    return f'dataset-name_sector-{ticker_bbg_index}-at{get_today("%Y%m%d")}-save{get_today("%Y%m%d")}.csv'

FILENAME_SECTOR_NAME = format_filename_of_name_sector
