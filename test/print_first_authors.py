#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:00:59 2019

@author: giudittaparolini
"""

import pandas as pd
import csv
from operator import itemgetter

#read the data
df = pd.read_csv("cleandata.csv")

#select only the column "Author" in the dataframe
authors = df["Author"]

#print the authors' names in a csv file
authors.to_csv("author.csv")

#open the csv files with the authors' names. In the file there are only two columns (row number and author names). The code reads the csv line by line
with open("author.csv", "r") as f:
    names = [line for line in csv.reader(f)]

#sort the authors' names alphabetically
names.sort(key=itemgetter(1))  # 1 being the column number

#overwrite the file with the authors listed in alphabetical order 
with open("author.csv", 'w') as f:
    csv.writer(f).writerows(names)

#load the csv with names in alphabetical order
df1 = pd.read_csv("author.csv")

#add column headers to the csv
df1.columns = ['Number', 'Name']

#generate a new csv with headers and data
df1.to_csv("author_headers.csv")

#load the csv generated above
df2 = pd.read_csv("author_headers.csv")

#drops the duplicate values considering only the column "Name"
df2.drop_duplicates(subset ="Name", inplace = True)

#drop the "Number" column and writes to a csv an alphabetical list without duplicates
df2.drop(["Number"], axis=1).to_csv("unique_author_names.csv")

#In the final csv there are two columns of numbers (they come, I think, from the intermediate csv). How can I get rid of them?

