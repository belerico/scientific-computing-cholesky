import os
import time
import numpy
from scipy import io
from scipy import linalg
from sksparse import cholmod

CWD = os.getcwd()
MATRICES_DIR = os.path.join(CWD, 'matrices')
RESULTS_DIR = os.path.join(CWD, 'results')

matrices = os.listdir(MATRICES_DIR)

for matrix in matrices:
    A = io.loadmat(os.path.join(MATRICES_DIR, matrix))['Problem']['A'][0][0]
    print('Resolving for ' + matrix)
    xe = numpy.ones([A.shape[0], 1])
    b = A * xe 
    """ L = linalg.cholesky(A, lower=True)
    y = linalg.solve(L, b)
    x = linalg.solve(numpy.transpose(L), y) """
    print('Decomposing matrix with Cholesky decomposition')
    start = time.time()
    factor = cholmod.cholesky(A)
    print('Done')
    print('Resolving equation Ax=b')
    x = factor(b)
    end = time.time()
    print('Done')
    if numpy.allclose(x, xe):
        e = linalg.norm(x -xe) / linalg.norm(xe)
        print('Error: ', e)
        print('Elapsed time:', str(end - start))
