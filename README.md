# scientific-computing-cholesky

Comparison between different scientific computing tool on the Cholesky decomposition.  
Steps for a proper installtion:

* `sudo apt install libsuitesparse-dev`. This is necessary if we want to work with a full-compatible library for Cholesky decomposition (scikit-sparse) of sparse matrices. One may want to install `libopenblas-dev and libopenblas-base` for multicore computation.
* Run `pip install pipenv`.
* Move to the `PROJECT_ROOT` folder.
* Run `pipenv install`; wait until locking phase is completed.
* Run `pipenv shell`.
* Run `python3 main.py --download-matrices`. This will run, for all our tool (python, MATLAB and Octave) and for all matrices the memory profiler and will generate the following directories:
  * `PROJECT_ROOT/results/matlab`
  * `PROJECT_ROOT/results/python`
  Each containing, for all matrices, the stats from the profiler

If you're running from Windows you have to disable `scikit-sparse` from Pipfile: that package must be manually compiled (<https://github.com/LyqSpace/Cholmod-Scikit-Sparse-Windows>).

Useful memory profiler:

* <https://github.com/pythonprofilers/memory_profiler>
* <https://github.com/astrofrog/psrecord>
