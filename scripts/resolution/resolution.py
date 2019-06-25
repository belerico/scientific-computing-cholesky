import os
import sys
import time
import numpy
import platform
from scipy import io, linalg
from cvxopt import cholmod, matrix, sparse
from cvxpy.interface import matrix_utilities
from memory_profiler import profile
from ..definitions import RESULTS_DIR, LOGS_DIR

matrix_path = sys.argv[1]
matrix_name = os.path.basename(matrix_path).split(".")[0]
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
log = open(os.path.join(LOGS_DIR, matrix_name + ".log"), "w+")


def read_mem(
        log_path: str, 
        line_from: int, 
        line_to: int, 
        column: int):
    assert line_to >= line_from
    assert column >= 0
    lines = open(log_path).readlines()[line_from:line_to]
    mem = 0
    for line in lines:
        splitted_line = line.split()
        # Do not consider empty lines and those commented out
        if len(splitted_line) > 1 and splitted_line[1] != "#":
            mem += float(splitted_line[column])
    return mem


# Get inline memory information 
@profile(stream=log)
def resolve(matrix_path):
    A = matrix_utilities.sparse2cvxopt(
            io.loadmat(matrix_path)["Problem"]["A"][0][0])
    xe = matrix(numpy.ones([A.size[0], 1]))
    b = sparse(A * xe)
    start = time.time()
    # scikit-sparse
    # factor = cholmod.cholesky(A)
    # x = factor(b)

    # linalg
    # factor = linalg.cholesky(A.todense())
    # x = linalg.cho_solve((factor, False), b)

    # cvxopt
    x = cholmod.splinsolve(A, b)
    end = time.time()
    elapsed = end - start
    return xe, x, elapsed


if __name__ == "__main__":
    """
                :param str sys.argv[1]: Matrix path to be loaded
        """
    results = "Resolving " + matrix_name + " matrix\n"
    xe, x, elapsed = resolve(matrix_path)
    log.flush()
    log.close()
    mem = read_mem(
            os.path.join(LOGS_DIR, matrix_name + ".log"), 
            6, 20, 3)

    rel_err = linalg.norm(x - xe) / linalg.norm(xe)
    results += "Relative error: " + str(rel_err) + "\n"
    results += "Elapsed time: " + str(elapsed) + " s\n"
    results += "Occupied memory: %.2f MiB\n\n" % mem

    f = open(
        os.path.join(
            RESULTS_DIR, 
            "python_" + str.lower(platform.system()) + "_result.txt"
        ),
        "a",
    )
    f.write(results)
    f.flush()
    f.close()
