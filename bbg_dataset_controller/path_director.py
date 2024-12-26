import os

def get_file_path(file_folder, file_name):
    return os.path.join(file_folder, file_name)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR = os.path.join(ROOT_DIR)

DATA_DIR = './data'
FILE_FOLDER_BBG = 'dataset-bbg'
FILE_FOLDER_SECTOR = 'dataset-sector'
FILE_FOLDER_MARKET = 'dataset-market'

file_folder = {
    'bbg': get_file_path(DATA_DIR, FILE_FOLDER_BBG),
    'sector': get_file_path(DATA_DIR, FILE_FOLDER_SECTOR),
    'market': get_file_path(DATA_DIR, FILE_FOLDER_MARKET),
}