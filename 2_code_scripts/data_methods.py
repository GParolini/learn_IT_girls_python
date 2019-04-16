#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""



#Remove the columns with more than 97 per cent NaNs. 
def drop_nans_col(df):
    df1 = df.loc[:, df.isnull().mean() <= .97]
    return df1

#Transform the numerical data in a column from floats to integers 
def colval_to_int(df, column):
    df[column] = (
    df[column].fillna(0)
    .astype(int)
    .astype(object)
    .where(df[column].notnull())
    )
    return df

#def get_journal_art_(df):
    #articles = df.loc[df["Item Type"] == "journalArticle"]
    #for article in articles:
        