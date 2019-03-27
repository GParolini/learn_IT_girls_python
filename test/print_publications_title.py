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

#select only the column "Publication Title" in the dataframe and eliminate the rows with nan values
publication_titles = df["Publication Title"].dropna()


#print the titles in a csv file
publication_titles.to_csv("publications.csv")

#open the csv file with the titles. In the file there are only two columns (row number and titles). The code reads the csv line by line
with open("publications.csv", "r") as f:
    publications = [line for line in csv.reader(f)]

#sort the titles alphabetically
publications.sort(key=itemgetter(1))  # 1 being the column number

#overwrite the file with the titles listed in alphabetical order 
with open("publications.csv", 'w') as f:
    csv.writer(f).writerows(publications)

#load the csv with titles in alphabetical order
df1 = pd.read_csv("publications.csv")

#add column headers to the csv
df1.columns = ['Number', 'Title']

#generate a new csv with headers and data
df1.to_csv("publications_headers.csv")

#load the csv generated above
df2 = pd.read_csv("publications_headers.csv")

#drops the duplicate values considering only the column "Title"
df2.drop_duplicates(subset ="Title", inplace = True)

#drop the "Number" column and writes to a csv an alphabetical list without duplicates
df2.drop(["Number"], axis=1).to_csv("unique_publications_names.csv")

#In the final csv there are two columns of numbers (they come, I think, from the intermediate csv). How can I get rid of them?
