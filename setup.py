import os
from setuptools import setup, find_packages
from definitions import BASE_DIR

requirementPath = os.path.join(BASE_DIR, 'requirements.txt')
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
setup(
    name='scientific_computing_chol', 
    version='1.0', 
    packages=find_packages(), 
    install_requires=install_requires
)