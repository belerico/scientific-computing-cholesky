# scientific-computing-cholesky

Comparison between different scientific computing tool on the Cholesky decomposition.  
Steps for a proper installtion:

* `python3 download-matrices.py`
* `sudo apt install libsuitesparse-dev`. This is necessary if we want to work with a full-compatible library for Cholesky decomposition (scikit-sparse) of sparse matrices
* `pip3 install -U py-install.txt`

Useful memory profiler:

* https://github.com/pythonprofilers/memory_profiler
* https://github.com/astrofrog/psrecord