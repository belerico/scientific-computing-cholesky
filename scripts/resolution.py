import os
import time
import numpy
from scipy import io
from scipy import linalg
from sksparse import cholmod
import platform

CWD = os.getcwd()
MATRICES_DIR = os.path.join(CWD, 'matrices')
RESULTS_DIR = os.path.join(CWD, 'results')
matrices = os.listdir(MATRICES_DIR)

def resolution(matrix):
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
        for matrix in matrices:
                results = 'Resolving for: ' + matrix + '\n'
                xe, x, elapsed = resolution(matrix)
                if numpy.allclose(x, xe):
                        e = linalg.norm(x -xe) / linalg.norm(xe)
                        results += 'Error: ' + str(e) + '\n'
                        results += 'Elapsed time: ' + str(elapsed) + '\n\n'
                else:
                        results += 'Solution is not even close to exact solution' + '\n\n'
                f = open(os.path.join(RESULTS_DIR, 'python_' + str.lower(platform.system()) + '_result.txt'), 'a')
                f.write(results)
                f.close()
