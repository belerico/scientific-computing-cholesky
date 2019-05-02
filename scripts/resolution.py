import os
import sys
import time
import numpy
import platform
from scipy import io
from scipy import linalg
from sksparse import cholmod

CWD = os.path.dirname(os.path.abspath(__file__))
MATRICES_DIR = os.path.join(CWD, '..', 'matrices')
RESULTS_DIR = os.path.join(CWD, '..', 'results')
matrices = os.listdir(MATRICES_DIR)

def resolve(matrix):
        A = io.loadmat(os.path.join(MATRICES_DIR, matrix))['Problem']['A'][0][0]
        xe = numpy.ones([A.shape[0], 1])
        b = A * xe 
        start = time.time()
        factor = cholmod.cholesky(A)
        x = factor(b)
        end = time.time()
        elapsed = end - start
        return xe, x, elapsed

if __name__ == '__main__':
        # for matrix in matrices:
        matrix = sys.argv[1]
        results = 'Resolving ' + matrix + '\n'
        xe, x, elapsed = resolve(matrix)
        if numpy.allclose(x, xe):
                e = linalg.norm(x -xe) / linalg.norm(xe)
                results += 'Error: ' + str(e) + '\n'
                results += 'Elapsed time: ' + str(elapsed) + ' s\n\n'
        else:
                results += 'Solution is not even close to exact solution' + '\n\n'
        f = open(os.path.join(RESULTS_DIR, 'python_' + str.lower(platform.system()) + '_result.txt'), 'a')
        f.write(results)
        f.close()
