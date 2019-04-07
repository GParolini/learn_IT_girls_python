#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""


#1 STRIP BLANK SPACES FROM ALL COLUMNS OF A DATAFRAME
def StripAllCols(df): 
    df.columns = df.columns.str.strip()

#2 STRIP BLANK SPACES FROM A SPECIFIC COLUMN OF A DATAFRAME
def StripCol(df,column): 
    df[column] = df[column].str.strip()



#3 PRINT TO FILE

#remove all the columns where more than 97 per cent of the cells are empty
df_clean1 = df.drop(df.loc[:,list((100*(df.isnull().sum()/len(df.index))>97))].columns, 1)

#remove the columns "Date added", "Date modified", "Access Date", "Library Catalog" and "Manual Tags" because not necessary
df_clean = df_clean1.drop( columns=["Date Added", "Date Modified", "Access Date", "Library Catalog", "Manual Tags"], axis = 1)

#Publication Years were transformed in floats in the previous passages. With the following code they are printed as integers again
df_clean["Publication Year"] = (
        df_clean["Publication Year"].fillna(0)
        .astype(int)
        .astype(object)
        .where(df_clean["Publication Year"].notnull())
        )

#print the resulting dataframe in a csv file
df_clean.to_csv(os.path.join("..","..", "1_data", "cleandata.csv"), mode="a")


#ITEMTYPE
import pandas as pd
import os

#read data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#list itemtypes labels in the data
item_types =list(set(df["Item Type"]))

df[(df[Item_type] = itemtype)]
print(item_types)




journal_articles = df.loc[df['Item Type'] == 'journalArticle']

journal_titles = journal_articles["Publication Title"].dropna()

journal_titles_unique = list(set(journal_titles))

journal_titles_unique.sort()


with open(os.path.join("..","..", "3_printouts", "journal_titles.txt"), 'w') as outfile:
    for title in journal_titles_unique:
        print(title, file=outfile)