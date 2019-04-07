#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:26:47 2019

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

#this UDF goes through every element of a list 
def printCoauthors(my_list):
    new_list = []
    for item in my_list:
        element = item.split(";")
        if element is not None and len(element)>1:
            new_list.append(element)
        else:
            continue
    for element in new_list:
        if element is not None:
            print(element) 
        else:
            continue
    

def search_nested(mylist, val):
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            print i,j
            if mylist[i][j] == val:
                return mylist[i]
    return str(val) + ' not found'


printCoauthors(author_list_no_duplicates)




#print(element, file=open(os.path.join("..","..", "3_printouts", "coauthors.txt"), "a"))