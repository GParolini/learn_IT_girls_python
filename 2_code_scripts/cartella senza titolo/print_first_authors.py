#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:00:59 2019

@author: giudittaparolini
"""

import pandas as pd
import os

#read the data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#select only the column "Author" in the dataframe and delete the rows with nan values
author_list = df["Author"].dropna()

#delete the duplicate names 
author_list_no_duplicates = list(set(author_list))

#sort in alphabetical orders (according to the first author)
author_list_no_duplicates.sort()

#open a txt file and write the list of titles in alphabetical order
with open(os.path.join("..","..", "3_printouts", "authors_list.txt"), 'w') as outfile:
    for author in author_list_no_duplicates:
        print(author, file=outfile)
