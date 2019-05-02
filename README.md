# scientific-computing-cholesky

Comparison between different scientific computing tool on the Cholesky decomposition.  
Steps for a proper installtion:

* `python3 download-matrices.py`
* `sudo apt install libsuitesparse-dev`. This is necessary if we want to work with a full-compatible library for Cholesky decomposition (scikit-sparse) of sparse matrices. One may want to install `libopenblas-dev and libopenblas-base` for multicore computation.
* `pip3 install -r requirements.txt`
* From `PROJECT_ROOT` run `python3 scripts/get-statistics.py`. This will run, for all our tool (python, MATLAB and Octave) and for all matrices the memory profiler and will generate the following directories:
  * `PROJECT_ROOT/results/matlab`
  * `PROJECT_ROOT/results/python`
  Each containing, for all matrices, the stats from the profiler

Useful memory profiler:

* https://github.com/pythonprofilers/memory_profiler
* https://github.com/astrofrog/psrecord
