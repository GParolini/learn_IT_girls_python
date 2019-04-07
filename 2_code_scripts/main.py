#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""

import pandas as pd
import os
import data_methods as dm
#import print_methods as pr
#import plot_methods as pl
#import utilities as ut


df = pd.read_csv(os.path.join("..", "1_data", "bibliography_data.csv"))

a = df.columns.tolist()

#col_names = df.dm.col_names()

with open(os.path.join("..", "3_printouts", "column_names.txt"),'w') as outfile:
    for item in a:
       print(item, file=outfile)

df1 = dm.drop_nans_col(df)
df2 = dm.drop_col_by_hand(df1, "Date Added")
df3 = dm.drop_col_by_hand(df2, "Date Modified")
df4 = dm.drop_col_by_hand(df3, "Access Date")
df5 = dm.colval_to_int(df4, "Publication Year")

df5.to_csv(os.path.join("..", "1_data", "cleandata.csv"))
