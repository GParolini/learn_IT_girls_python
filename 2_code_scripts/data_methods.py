#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""

def col_names(df):
    """Print columns' headers 
    """
    df.columns.tolist()
    return

def drop_nans_col(df):
    """Remove the columns with more than 97 per cent NaNs. 
    """
    df1 = df.loc[:, df.isnull().mean() <= .97]
    return df1

def drop_col_by_hand(df,col):
    """Remove the column passed in the argument. 
    """
    df1 = df.drop(columns = [col], axis = 1)
    return df1

 
def colval_to_int(df, column):
    """Transform the numerical data in a column from floats to integers 
    """
    df[column] = (
        df[column].fillna(0)
        .astype(int)
        .astype(object)
        .where(df[column].notnull())
        )
    return df

#remove the columns "Date added", "Date modified", "Access Date", "Library Catalog" and "Manual Tags" because not necessary
#df_clean = df_clean1.drop( columns=["Date Added", "Date Modified", "Access Date", "Library Catalog", "Manual Tags"], axis = 1)

#Publication Years were transformed in floats in the previous passages. With the following code they are printed as integers again
#df_clean["Publication Year"] = (
        #df_clean["Publication Year"].fillna(0)
        #.astype(int)
        #.astype(object)
        #.where(df_clean["Publication Year"].notnull())
        #)

#print the resulting dataframe in a csv file
#df_clean.to_csv(os.path.join("..","..", "1_data", "cleandata.csv"), mode="a")


#ITEMTYPE
#import pandas as pd
#import os

#read data
#df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#list itemtypes labels in the data
#item_types =list(set(df["Item Type"]))

#df[(df[Item_type] = itemtype)]
#print(item_types)




#journal_articles = df.loc[df['Item Type'] == 'journalArticle']

#journal_titles = journal_articles["Publication Title"].dropna()

#journal_titles_unique = list(set(journal_titles))

#journal_titles_unique.sort()


#with open(os.path.join("..","..", "3_printouts", "journal_titles.txt"), 'w') as outfile:
    #for title in journal_titles_unique:
        #print(title, file=outfile)