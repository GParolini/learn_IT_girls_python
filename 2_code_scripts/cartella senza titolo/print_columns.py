#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""

import pandas as pd
import os

#import the full dataset
df = pd.read_csv(os.path.join("..","..", "1_data", "bibliography_data.csv"))

#print in a csv file the columns of the df and their type
df.dtypes.to_csv(os.path.join("..","..", "3_printouts", "columns.csv"), mode="a")

#A FEW USEFUL METHODS WITH COLUMNS

#method for changing the item type from float to integer. Where is the mistake? I cannot understand!
def float_to_int (column):
    for x in column
    print int(x) if type(x) == float
     
    
