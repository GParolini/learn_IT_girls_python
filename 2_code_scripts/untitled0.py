#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 07:51:10 2019

@author: giudittaparolini
"""
import pandas as pd
import os
import data_methods as dm
import print_methods as pr
import plot_methods as pl
import utilities as ut
import csv

#Load the data
df = pd.read_csv(os.path.join("..", "1_data", "bibliography_data.csv"))

df_cat = pd.read_csv(os.path.join("..", "1_data", "corr_journ_cat.csv"))
df2 = df_cat.drop(['Category2', 'Language'], axis=1)
#print (df2)

def get_journal_cat(df,df_cat):
    df1 = df.loc[df["Item Type"] == "journalArticle"]
    df2 = df_cat.drop(['Category2', 'Language'], axis=1)
    df3 = df1.merge(df2, on='Publication Title')
    return df3

def cat_count_list():
    with open(os.path.join("..", "1_data","df_jour_cat.csv")) as f:
        reader = csv.reader(f)
        my_list = list(reader)
        return my_list

def main_cat_list():
    with open(os.path.join("..", "1_data","df_jour_cat.csv")) as f:
        reader = csv.reader(f)
        cat_count_list = list(reader)
    my_list = cat_count_list()
    agg_list = []
    for item in my_list[0:5]:
        agg_list.append(item)
    return agg_list



a = main_cat_list()
print(a)