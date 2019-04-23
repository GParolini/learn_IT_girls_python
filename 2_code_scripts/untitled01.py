#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:14:40 2019

@author: giudittaparolini
"""
import pandas as pd
import os
import seaborn as sns


def scatter_grouped_l():
    col_val = ["Category", "Publication Year", "Count"]
    df_cat = pd.read_csv(os.path.join("..", "3_printouts", "jourcat_year_counts.csv"),names = col_val)
    print(df_cat)
    df_cat_l = df_cat.loc[(df_cat['Publication Year'] >= 1925) & (df_cat['Publication Year'] <= 1935)]
    #df_drop_rows_1925 = df_cat[(df_cat["Publication Year"]<1925)]
    #df_drop_rows_1935 = df_cat[(df_cat["Publication Year"]>1935)]
    #df_cat_l1 = df_cat.drop(df_drop_rows_1925.index, axis=0)
    #df_cat_l2 = df_cat_l1.drop(df_drop_rows_1935.index, axis=0)
    sns.scatterplot(x="Publication Year", y="Category", hue = "Count", legend = False, data=df_cat_l)
    
    
a = scatter_grouped_l()

print(a)