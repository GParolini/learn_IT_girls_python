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

#select only the column "Publication Title" in the dataframe and eliminate the rows with nan values
publication_titles = df["Publication Title"].dropna()

#transform the list into a set (that automatically takes care of eliminating duplicates)
publication_title_no_duplicates = set(publication_titles)

#re-transform the set into a list
publication_title_no_duplicates_list = list(set(publication_titles))

#sort the list of publications in alphabetical order
publication_title_no_duplicates_list.sort()

#open a txt file and write the list of titles in alphabetical order
with open(os.path.join("..","..", "3_printouts", "publication_titles.txt"), 'w') as outfile:
    for title in publication_title_no_duplicates_list:
        print(title, file=outfile)

