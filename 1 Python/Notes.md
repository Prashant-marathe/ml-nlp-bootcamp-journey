Creating virtual environments using python
Using Python:
    - Python -m venv <environment name>
    - <environment name>\Scripts\activate
    - deactivate

Using virtualenv package (specifically for linux)
    - pip install virtualenv
    - virtualenv -p python3 <environment name>
    - <environment name>\Scripts\activate
    - deactivate 
    
Using conda environment
    - conda create -p <enviroment name> python==3.10 -y
    - conda activate <environment name>
    - conda deactivate

Modules in Python
import math
from math import sqrt
from math import *

Creating own custom module 
1] create a external folder with a __init__.py file
2] create your python file and define your code
3] to use that files functions and variables you need to import it wherever you want
    from <foldername.filename> import <functions variables>
    