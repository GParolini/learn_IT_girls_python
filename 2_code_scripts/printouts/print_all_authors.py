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

#split the multiple values in the cells of the column "Author" e produces a new dataframe where there are duplicated rows for the splitted values 
reshaped = \
(df.set_index(df.columns.drop("Author",1).tolist())
   .Author.str.split('; ', expand=True)
   .stack()
   .reset_index()
   .rename(columns={0:'Author'})
   .loc[:, df.columns]
)

#select only the column "Author" and drop the nan values
authors = reshaped["Author"].dropna()

#strip the empty spaces at the beginning and at the end of the column entries, otherwise the system cannot sort alphabetically (sort also the white spaces)
authors1 = authors.str.strip(" ")

#use list and set to produce a list of unique author's names
authors_noduplicates = list(set(authors1))

#sort the names in alphabetical order
authors_noduplicates.sort()


#open a txt file and write the list of titles in alphabetical order
with open(os.path.join("..","..", "3_printouts", "authors_all_list.txt"), 'w') as outfile:
    for author in authors_noduplicates:
        print(author, file=outfile)
