import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
MATRICES_DIR = os.path.join(BASE_DIR, 'matrices')

if __name__ == '__main__':
    print(BASE_DIR)