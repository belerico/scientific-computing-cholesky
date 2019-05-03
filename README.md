# scientific-computing-cholesky

Comparison between different scientific computing tool on the Cholesky decomposition.  
Steps for a proper installtion:

* `sudo apt install libsuitesparse-dev`. This is necessary if we want to work with a full-compatible library for Cholesky decomposition (scikit-sparse) of sparse matrices. One may want to install `libopenblas-dev and libopenblas-base` for multicore computation.
* It's recommended to have virtualenv installed, if not you could install it by running `pip install virtualenv`. Move to the `PROJECT_ROOT` folder and run `virtualenv venv`.
* After that you have to install the project itself: `python setup.py install`
* Run `python scripts/tool_profiling --download-matrices`. This will run, for all our tool (python, MATLAB and Octave) and for all matrices the memory profiler and will generate the following directories:
  * `PROJECT_ROOT/results/matlab`
  * `PROJECT_ROOT/results/python`
  Each containing, for all matrices, the stats from the profiler

Useful memory profiler:

* <https://github.com/pythonprofilers/memory_profiler>
* <https://github.com/astrofrog/psrecord>
