import os
from os import path
import platform
import subprocess

CWD = path.dirname(path.abspath(__file__))
BASE_DIR = path.normpath(path.join(CWD, '..', '.'))
MATRICES_DIR = path.join(BASE_DIR, 'matrices')
RESULTS_DIR = path.join(BASE_DIR, 'results')
OS = platform.system().lower()
matrices = os.listdir(MATRICES_DIR)

if __name__ == '__main__':
    for tool in ['python']:
        if not(path.exists(path.join(RESULTS_DIR, tool, OS))):
                os.makedirs(path.join(RESULTS_DIR, tool, OS))
        for matrix in ['Flan_1565.mat']:
            command = 'mprof run --include-children --interval 0.05 --output ' + path.join(RESULTS_DIR, tool, OS, matrix.split('.')[0] + '.txt') + ' '
            if tool == 'matlab':
                # command = 'psrecord "matlab -nodisplay -nosplash -nodesktop -r \\"addpath(genpath(pwd));resolution(\'' + matrix + '\');exit;\\"" '
                command += 'matlab -nodisplay -nosplash -nodesktop -r "addpath(genpath(\'' + BASE_DIR + '\'));resolution(\'' + matrix + '\');exit;"'
            elif tool == 'python':
                # command = 'psrecord "python3 ' + path.join(CWD, 'resolution.py') + ' ' + matrix + '" '
                command += path.join(CWD, 'resolution.py') + ' \
                    ' + path.join(MATRICES_DIR, matrix) + ' \
                    ' + RESULTS_DIR
            """ command += '--include-children \
                        --interval 0.05 \
                        --log ' + path.join(RESULTS_DIR, tool, OS, matrix.split('.')[0] + '.txt') """
            proc = subprocess.call(command, shell=True)