#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""

import os
import matplotlib.pyplot as plt

# PRINT TO A CSV FILE IN THE FOLDER 1_DATA
def print_csv_data (df, filename):
     df.to_csv(os.path.join("..", "1_data", filename))


#1 PRINT TO A TXT FILE IN THE FOLDER 3_PRINTOUTS
def print_txt_printouts (to_be_printed, filename):
        with open(os.path.join("..", "3_printouts", filename),'w') as outfile:
            for item in to_be_printed:
                print(item, file=outfile)
       
# PRINT TO A CSV FILE IN THE FOLDER 3_PRINTOUTS
def print_csv_printouts (df, filename):
     df.to_csv(os.path.join("..", "3_printouts", filename))

# PRINT A JPG FIGURE IN THE FOLDER 4_PLOTS
def print_plot (fig, filename):
    plt.savefig(os.path.join("..", "4_plots", filename))




#1 STRIP BLANK SPACES FROM ALL COLUMNS OF A DATAFRAME
def StripAllCols(df): 
    df.columns = df.columns.str.strip()

#2 STRIP BLANK SPACES FROM A SPECIFIC COLUMN OF A DATAFRAME
def StripCol(df,column): 
    df[column] = df[column].str.strip()