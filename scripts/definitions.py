from os import path

BASE_DIR = path.dirname(path.normpath(path.join(path.abspath(__file__), '..')))
RESULTS_DIR = path.join(BASE_DIR, 'results')
MATRICES_DIR = path.join(BASE_DIR, 'matrices')
LOGS_DIR = path.join(BASE_DIR, 'logs')