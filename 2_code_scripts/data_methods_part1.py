#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""

""" 
Methods for the pre-processing of the bibliography data 
"""

#Remove the columns with more than 97 per cent NaNs. 
def drop_nans_col(df):
    df1 = df.loc[:, df.isnull().mean() <= .97]
    return df1

#Transform the numerical data in a column from floats to integers (useful with the "Date" column because integers are trasformed in floats by pandas)
def colval_to_int(df, column):
    df[column] = (
    df[column].fillna(0)
    .astype(int)
    .astype(object)
    .where(df[column].notnull())
    )
    return df








        