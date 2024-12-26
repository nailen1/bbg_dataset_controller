from shining_pebbles import open_df_in_file_folder_by_regex
from .path_director import file_folder

# def get_df_members_of_bbg_index(ticker_bbg_index, save=True):
#     fld = 'INDX_MEMBERS'
#     df = bcon.bulkref(tickers=[ticker_bbg_index], flds=[fld])
#     df = df[['ticker', 'value']]
#     df.columns = ['ticker_bbg_index', fld]
#     df = df.set_index('ticker_bbg_index')
#     if save:
#         save_dataset_of_subject_at(df, file_folder='dataset-bbg', subject=f'bbg-{ticker_bbg_index}-{fld}', input_date=get_today("%Y%m%d"))
#     return df

# def get_df_names_of_bbg_index(ticker_bbg_index, save=True):
#     df_names = get_df_fld_of_bbg_index(ticker_bbg_index=ticker_bbg_index, fld='NAME', save=save)
#     return df_names

# def get_df_names_kr_of_bbg_index(ticker_bbg_index, save=True):
#     df_names = get_df_fld_of_bbg_index(ticker_bbg_index=ticker_bbg_index, fld='NAME_KOREAN', save=save)
#     return df_names

# def get_df_sector_of_bbg_index(ticker_bbg_index, save=True):
#     df_sector = get_df_fld_of_bbg_index(ticker_bbg_index=ticker_bbg_index, fld='GICS_SECTOR_NAME', save=save)
#     return df_sector

def get_tickers_bbg_index(tickers):
    tickers_bbg = [f'{ticker} Equity' for ticker in tickers]
    return tickers_bbg

# def get_df_fld_of_bbg_index(ticker_bbg_index, fld, save=False):
#     df_members = open_df_in_file_folder_by_regex('dataset-bbg', regex=f'bbg-{ticker_bbg_index}-INDX_MEMBERS-at{get_today("%Y%m%d")[:-2]}')
#     tickers_bbg = get_tickers_bbg_index(df_members['INDX_MEMBERS'])
#     flds = [fld]
#     df = bcon.ref(tickers=tickers_bbg, flds=flds)
#     df = df[['ticker', 'value']]
#     df.columns = ['ticker_bbg', fld]
#     df_fld = df.set_index('ticker_bbg', drop=True)
#     if save:
#         save_dataset_of_subject_at(df_fld, file_folder='dataset-bbg', subject=f'bbg-{ticker_bbg_index}-{fld}', input_date=get_today("%Y%m%d"))
#     return df_fld

def open_df_fld_of_bbg_index(ticker_bbg_index, fld):
    df = open_df_in_file_folder_by_regex(file_folder=file_folder['bbg'], regex=f'{ticker_bbg_index}-{fld}-')
    return df

def open_df_name_of_bbg_index(ticker_bbg_index):
    df = open_df_fld_of_bbg_index(ticker_bbg_index=ticker_bbg_index, fld='NAME')
    return df

def open_df_name_kr_of_bbg_index(ticker_bbg_index):
    df = open_df_fld_of_bbg_index(ticker_bbg_index=ticker_bbg_index, fld='NAME_KOREAN')
    return df

def open_df_sector_of_bbg_index(ticker_bbg_index):
    df = open_df_fld_of_bbg_index(ticker_bbg_index=ticker_bbg_index, fld='GICS_SECTOR_NAME')
    return df
