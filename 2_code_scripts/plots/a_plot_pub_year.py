#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:09:31 2019

@author: giudittaparolini
"""

#adding the building blocks of my code/1: pandas
import pandas as pd

#adding the building blocks of my code/2: mathplotlib
from matplotlib import pyplot as plt

#adding the building blocks of my code/3: pathlib to write file paths more easily
from pathlib import Path
#data_folder = Path("4_plots" / "1_data")

home_folder = Path.home()
data_dir = Path.() /"1_data"  
#print(current_dir)  
print(data_dir) 


