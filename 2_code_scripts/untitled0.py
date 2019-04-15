#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:39:47 2019

@author: giudittaparolini
"""
import pandas as pd
import os

df = pd.read_csv(os.path.join("..", "1_data", "bibliography_data.csv"))
my_list = open (os.path.join("..", "3_printouts", "first_authors.txt"), "r")

def print_all_authors(df):
    reshaped = \
    (df.set_index(df.columns.drop("Author",1).tolist())
    .Author.str.split('; ', expand=True)
    .stack()
    .reset_index()
    .rename(columns={0:'Author'})
    .loc[:, df.columns]
    )
    authors = reshaped["Author"].dropna()
    authors1 = authors.str.strip(" ")
    authors_noduplicates = list(set(authors1))
    return sorted(authors_noduplicates)

b = print_all_authors(df)
print(b)

def print_multiauthors(my_list):
    new_list = []
    for item in my_list:
        element = item.split(";")
        if element is not None and len(element)>1:
            new_list.append(element)
        else:
            continue
    return new_list

a = print_multiauthors(my_list)
print(a)

def print_coauthors(mylist, all_authors_list):
    coauthors = []
    for item in mylist:
        for author in all_authors_list:
            if item.count(author)>0:
                coauthors.extend(item)
            else:
                continue
            return coauthors

#with open(os.path.join("..", "3_printouts", "multiauthors.txt"),'w') as outfile:
        #for item in a:
            #print(item, file=outfile)

c = print_coauthors(a, b)

print(c)

#print(a)

#def search_coauthors(mylist, val):
    #for i in range(len(mylist)):
        #for j in range(len(mylist[i])):
            #print (i,j)
            #if mylist[i][j] == val:    
            #if mylist[j] == val:
                #print(mylist[i])

                
            #else:
                #continue
            #return print(mylist[i])
                #return mylist[i]
            #else:
                #continue
            #return str(val) + ' not found'
                #print (str(val) + ' not found')
    #return coauthors

#b = search_coauthors(a, "Allard, H. A.")
#print (b)
#def print_coauthors(mylist):