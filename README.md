# scientific-computing-cholesky

Comparison between different scientific computing tool on the Cholesky decomposition.  
Steps for a proper installtion:

* Get [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and install it
* Clone this repository with `git clone https://github.com/belerico/scientific_computing_cholesky,git`
* Move to the `PROJECT_ROOT` folder
* Run `conda env create -f environment.yml`; if some packages are not found, remove them from the environment.yml file and rerun the above command
* Run `conda activate cholesky`
* Run `python main.py --download-matrices`. This will run, for all our tool (python, MATLAB and Octave) and for all matrices the memory profiler and will generate the following directories:
  * `PROJECT_ROOT/results/matlab`
  * `PROJECT_ROOT/results/octave`
  * `PROJECT_ROOT/results/python`
    Each containing, for all matrices, the stats from the profiler

Useful memory profiler:

* <https://github.com/pythonprofilers/memory_profiler>
* <https://github.com/astrofrog/psrecord>
