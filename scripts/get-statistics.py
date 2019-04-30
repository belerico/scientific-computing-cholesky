import os
import platform
import subprocess

CWD = os.path.dirname(os.path.abspath(__file__))
MATRICES_DIR = os.path.join(CWD, '..', 'matrices')
RESULTS_DIR = os.path.join(CWD, '..', 'results')
OS = platform.system().lower()
matrices = os.listdir(MATRICES_DIR)

if __name__ == '__main__':
    for tool in ['python', 'matlab']:
        if not(os.path.exists(os.path.join(RESULTS_DIR, tool, OS))):
                os.makedirs(os.path.join(RESULTS_DIR, tool, OS))
        for matrix in matrices:
            command = ''
            if tool == 'matlab':
                command = 'psrecord "matlab -nodisplay -nosplash -nodesktop -r \\"addpath(genpath(pwd));resolution(\'' + matrix + '\');exit;\\"" '
            elif tool == 'python':
                command = 'psrecord "python3 ' + os.path.join(CWD, 'resolution.py') + ' ' + matrix + '" '
            command += '--include-children \
                        --interval 0.05 \
                        --log ' + os.path.join(RESULTS_DIR, tool, OS, matrix.split('.')[0] + '.txt')
            proc = subprocess.call(command, shell=True)