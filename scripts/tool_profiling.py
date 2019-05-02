import os
from os import path
import platform
import subprocess
from download_matrices import download_matrices
from scripts.get_statistics import get_statistics

CWD = path.dirname(path.abspath(__file__))
BASE_DIR = path.normpath(path.join(CWD, '..', '.'))
MATRICES_DIR = path.join(BASE_DIR, 'matrices')
RESULTS_DIR = path.join(BASE_DIR, 'results')
OS = platform.system().lower()
matrices = sorted(os.listdir(MATRICES_DIR), key=str.lower)

if __name__ == '__main__':
    download_matrices()
    for tool in ['python', 'matlab', 'octave']:
        if not(path.exists(path.join(RESULTS_DIR, tool, OS))):
                os.makedirs(path.join(RESULTS_DIR, tool, OS))
        for matrix in matrices:
            command = 'mprof run --include-children --interval 0.05 --output ' + path.join(RESULTS_DIR, tool, OS, matrix.split('.')[0] + '.txt') + ' '
            if tool == 'python':
                # command = 'psrecord "python3 ' + path.join(CWD, 'resolution.py') + ' ' + matrix + '" '
                command += path.join(CWD, 'resolution.py') + ' \
                    ' + path.join(MATRICES_DIR, matrix) + ' \
                    ' + RESULTS_DIR
            elif tool == 'matlab':
                # command = 'psrecord "matlab -nodisplay -nosplash -nodesktop -r \\"addpath(genpath(pwd));resolution(\'' + matrix + '\');exit;\\"" '
                command += 'matlab -nodisplay -nosplash -nodesktop -r "addpath(genpath(\'' + BASE_DIR + '\'));resolution(\'' + matrix + '\', \'matlab\');exit;"'
            else:
                command += 'octave --no-gui --eval "addpath(genpath(\'' + BASE_DIR + '\'));resolution(\'' + matrix + '\', \'octave\');"'
            """ command += '--include-children \
                        --interval 0.05 \
                        --log ' + path.join(RESULTS_DIR, tool, OS, matrix.split('.')[0] + '.txt') """
            proc = subprocess.call(command, shell=True)
    get_statistics(BASE_DIR, RESULTS_DIR)
    