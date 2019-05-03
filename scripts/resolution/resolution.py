import os
import sys
import time
import numpy
import platform
import tracemalloc
from scipy import io
from scipy import linalg
from sksparse import cholmod
from definitions import RESULTS_DIR


def resolve(matrix):
        tracemalloc.start()
        A = io.loadmat(matrix)['Problem']['A'][0][0]
        xe = numpy.ones([A.shape[0], 1])
        b = A * xe 
        start = time.time()
        factor = cholmod.cholesky(A)
        x = factor(b)
        end = time.time()
        snapshot = tracemalloc.take_snapshot()
        stats = snapshot.statistics('lineno')
        mem = sum(stat.size for stat in stats)
        elapsed = end - start
        return xe, x, elapsed, mem


if __name__ == '__main__':
        """
                :param str sys.argv[1]: Matrix path to be loaded
        """
        matrix = sys.argv[1]
        results = 'Resolving ' + os.path.basename(matrix) + '\n'
        xe, x, elapsed, mem = resolve(matrix)
        if numpy.allclose(x, xe):
                e = linalg.norm(x -xe) / linalg.norm(xe)
                results += 'Error: ' + str(e) + '\n'
                results += 'Elapsed time: ' + str(elapsed) + ' s\n'
                results += 'Occupied memory: %.2f MiB\n\n' % (mem / (1024 ** 2))
        else:
                results += 'Solution is not even close to exact solution' + '\n\n'
        f = open(os.path.join(RESULTS_DIR, 'python_' + str.lower(platform.system()) + '_result.txt'), 'a')
        f.write(results)
        f.close()
