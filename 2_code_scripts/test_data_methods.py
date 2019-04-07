#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""
import pandas as pd
import os

df = pd.read_csv(os.path.join("..", "1_data", "bibliography_data.csv"))
print(df.columns.tolist())


def drop_col_by_hand(df,col):
    """Remove the list of columns passed in the argument. 
    """
    df1 = df.drop(columns = [col], axis = 1)
    return df1
    #df.columns.tolist()
    #df.drop([col for col in col_list], axis=1, inplace=True)
    #return

#print(drop_col_by_hand(df,["Date Added"]))

df1 = drop_col_by_hand(df,'Date Added')
df2 = drop_col_by_hand(df1,'Date Modified')

#print the resulting dataframe in a csv file
df2.to_csv(os.path.join("cleandata.csv"), mode="w")

#import pandas as pd

# Create an example DataFrame
#data = [
    #[1, 'ABC', 4, 10, 6.3],
    #[2, 'BCD', 10, 9, 11.6],
    #[3, 'CDE', 7, 4, 10.0],
    #[4, 'DEF', 7, 10, 5.4],
    #[5, 'EFG', 2, 9, 5.3],
#]
#data = pd.DataFrame(data, 
    #columns = ['Id', 'Name', 'Rating1', 'Rating2', 'ThisIsANumber'])

# Just want columns Id and Ratings2
#new_data = data.drop(['Name', 'Rating1', 'ThisIsANumber'], axis = 1)
#new_data.head()

# ** It would be nice to be able to only specify the columns we want 
# ** to keep to save typing - similar to dplyr in R             

#def keep_cols(DataFrame, keep_these):
    #"""Keep only the columns [keep_these] in a DataFrame, delete
    #all other columns. 
    #"""
   # drop_these = list(set(list(DataFrame)) - set(keep_these))
    #return DataFrame.drop(drop_these, axis = 1)

#new_data = data.pipe(keep_cols, ['Id', 'Rating2'])
#new_data.head()

# In this specific example there was not much more typing between
# `.drop` and the `keep_cols` function, but often when a `DataFrame`
# has many columns this is not the case!