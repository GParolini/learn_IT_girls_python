

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019
@author: giudittaparolini
"""

import pandas as pd
import os

df = pd.read_csv(os.path.join("..","..", "1_data", "bibliography_data.csv"))

print()

#remove empty spaces at the beginning/end of column headers [the code gave an error otherwise]
df.columns = df.columns.str.strip()

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