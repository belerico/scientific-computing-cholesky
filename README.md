# scientific-computing-cholesky

Comparison between different scientific computing tool on the Cholesky decomposition.  
Steps for a proper installtion:

* Get [MATLAB](https://it.mathworks.com/downloads/)
* Get [Octave](https://www.gnu.org/software/octave/download.html) for your operating system: in case you run a linux distribution you msy install Octave from [Flathub](https://flathub.org/apps/details/org.octave.Octave), this is due to the fact that many distributions doens't have the latest Octave release in their official repositories
* Get [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and install it for your operating system
* Clone this repository with `git clone https://github.com/belerico/scientific_computing_cholesky.git`
* Move to the `PROJECT_ROOT` folder
* Run `conda env create -f environment.yml`; if some packages are not found, remove them from the environment.yml file and rerun the above command
* Run `conda activate cholesky`
* Run `python main.py --help` to get all possible command one may execute
* Run `python main.py --download-matrices`. This will run, for all our tool (python, MATLAB and Octave) and for all matrices the memory profiler and will generate the following directories, each containing, for all matrices, the stats from the profiler:

  * `PROJECT_ROOT/results/matlab`
  * `PROJECT_ROOT/results/octave`
  * `PROJECT_ROOT/results/python`  

Useful memory profiler:

* <https://github.com/pythonprofilers/memory_profiler>
* <https://github.com/astrofrog/psrecord>
