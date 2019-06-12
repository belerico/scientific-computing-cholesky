import os
import shutil
import argparse
import platform
import subprocess
from os import path
from scripts.utils.get_statistics import get_statistics
from scripts.utils.download_matrices import download_matrices
from scripts.definitions import BASE_DIR, MATRICES_DIR, RESULTS_DIR, SCRIPTS_DIR

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', 
    '--download-matrices', 
    help='download required matrices', 
    action='store_true'
)
parser.add_argument(
    '-i',
    '--interval', 
    default='0.05', 
    type=str, 
    help='sampling interval in seconds', 
    action='store'
)
parser.add_argument(
    '-o', 
    '--output', 
    default=RESULTS_DIR, 
    type=str, 
    help='path to store results', 
    action='store'
)
args = parser.parse_args()
if args.download_matrices:
    download_matrices()

OS = platform.system().lower()
matrices = sorted(os.listdir(MATRICES_DIR), key=str.lower)
# Remove previous results 
if path.exists(RESULTS_DIR):
    shutil.rmtree(RESULTS_DIR)
for tool in ['python', 'octave', 'matlab']:
    if not(path.exists(path.join(args.output, tool, OS))):
            os.makedirs(path.join(args.output, tool, OS))
    for matrix in matrices:
        # command = 'mprof run \
        #             --include-children \
        #             --interval ' + args.interval + ' \
        #             --output ' + path.join(args.output, tool, OS, matrix.split('.')[0] + '.txt') + ' '
        command = 'python ' + path.join(SCRIPTS_DIR, 'record.py') + ' \
                    --include-children \
                    --log ' + path.join(args.output, tool, OS, matrix.split('.')[0] + '.txt') + ' \
                    --interval ' + args.interval + ' '
        if tool == 'python':
            command += '"python -m scripts.resolution.resolution ' + path.join(MATRICES_DIR, matrix) + '"'
            # command += path.join(BASE_DIR, 'scripts', 'resolution', 'resolution.py') + ' ' + path.join(MATRICES_DIR, matrix)
        elif tool == 'matlab':
            # command = 'psrecord "matlab -nodisplay -nosplash -nodesktop -r \\"addpath(genpath(pwd));resolution(\'' + matrix + '\');exit;\\"" '
            command += '"matlab \
                        -wait \
                        -nodisplay \
                        -nosplash \
                        -nodesktop \
                        -r \\"addpath(genpath(\'' + BASE_DIR + '\')); \
                            cd \'' + BASE_DIR + '\'; \
                            resolution(\'' + matrix + '\', \'matlab\'); \
                            exit;\\""'
        else:
            command += '"octave-cli \
                        --no-gui \
                        --eval \\"addpath(genpath(\'' + BASE_DIR + '\')); \
                            cd \'' + BASE_DIR + '\'; \
                            resolution(\'' + matrix + '\', \'octave\');\\""'
        cmd = subprocess.Popen(command, shell=True)
        cmd.communicate()
get_statistics(args.output)
    