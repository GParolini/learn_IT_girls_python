#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:14:09 2019

@author: giudittaparolini
"""
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import utilities as ut


#Plot the histogram for the publications printed in each year
def hist_pub_year(df):
    plt.figure(figsize=(25,14))
    df.hist(column="Publication Year", bins=50 )
    plt.xlabel("Publication Year",fontsize=15)
    plt.ylabel("Frequency",fontsize=15)
    
#Plot the histogram of the publications' languages
def count_plot_lang(df):
     sns.set(style="darkgrid")
     sns.set(rc={"figure.figsize":(25,14)})
     sns.countplot(y="Language", data=df)

#Plot pie chart of the publications' languages
def pie_lang():
    my_list = ut.agg_list()
    languages = dict(my_list).keys()
    counts = dict(my_list).values()
    
    plt.figure(figsize=(10,8))      
    explode = (0.1,0,0,0,0,0)
    plt.pie(counts, explode, 
            autopct='%1.1f%%', pctdistance=0.7, shadow=True, startangle=140)
    plt.title("Publications distributed according to language")
    plt.legend(loc="best", labels=languages )
    plt.axis('equal')
    
#Plot pie chart of the journal categories
def pie_jcat():
    my_list = ut.agg_jcat_list()
    jcat = dict(my_list).keys()
    counts = dict(my_list).values()
    
    plt.figure(figsize=(10,8))      
    explode = (0,0,0,1.0,0,0)
    plt.pie(counts, explode, 
            autopct='%1.1f%%', pctdistance=0.7, shadow=True, startangle=140)
    plt.title("Articles distributed according to journal category")
    plt.legend(loc="best", labels=jcat )
    plt.axis('equal')

    
#Scatter plot for evolution of categories
def scatter_jcat():
    col_val = ["Category", "Publication Year", "Count"]
    df_cat = pd.read_csv(os.path.join("..", "3_printouts", "jourcat_year_counts.csv"),names = col_val)
    plt.figure(figsize=(25,14))
    plt.scatter(df_cat["Publication Year"],df_cat["Category"], s=df_cat["Count"])

    
#Scatter plot for evolution of categories limited to the years 1925-1935
def scatter_jcat_l():
    col_val = ["Category", "Publication Year", "Count"]
    df_cat = pd.read_csv(os.path.join("..", "3_printouts", "jourcat_year_counts.csv"),names = col_val)
    df_drop_rows_1925 = df_cat[(df_cat["Publication Year"]<1925)]
    df_drop_rows_1935 = df_cat[(df_cat["Publication Year"]>1935)]
    df_cat_l1 = df_cat.drop(df_drop_rows_1925.index, axis=0)
    df_cat_l = df_cat_l1.drop(df_drop_rows_1935.index, axis=0)
    plt.figure(figsize=(25,14))
    plt.scatter(df_cat_l["Publication Year"],df_cat_l["Category"], s=df_cat_l["Count"])

    
#Scatter plot for evolution of categories grouped
def scatter_grouped():
    col_val = ["Category", "Publication Year", "Count"]
    df_cat = pd.read_csv(os.path.join("..", "3_printouts", "jourcat_year_counts.csv"),names = col_val)
    sns.scatterplot(x="Publication Year", y="Category", hue = "Count", legend = False, data=df_cat)
    
#Scatter plot for evolution of categories limited to the years 1925-1935 and grouped
def scatter_grouped_lg():
    col_val = ["Category", "Publication Year", "Count"]
    df_cat = pd.read_csv(os.path.join("..", "3_printouts", "jourcat_year_counts.csv"),names = col_val)
    df_cat_lg = df_cat.loc[(df_cat["Publication Year"] == 1925) | (df_cat["Publication Year"] == 1930) | (df_cat["Publication Year"] == 1935)]
    sns.scatterplot(x="Publication Year", y="Category", hue="Count", legend = "full", data=df_cat_lg)
    
#Line plot
def line_jcat():
    col_val = ["Category", "Publication Year", "Count"]
    df_cat = pd.read_csv(os.path.join("..", "3_printouts", "jourcat_year_counts.csv"),names = col_val)
    plt.figure(figsize=(25,14)) 
    sns.lineplot(x="Publication Year", y="Count", hue="Category", data=df_cat)
    
#Line plot main categories
def line_jcat_main():
    col_val = ["Category", "Publication Year", "Count"]
    df_cat = pd.read_csv(os.path.join("..", "3_printouts", "jourcat_year_counts.csv"),names = col_val)
    df_cat_main = df_cat.loc[(df_cat["Category"] == "Agriculture") | (df_cat["Category"] == "Botany/Plant Breeding") | (df_cat["Category"] == "Meteorology") | (df_cat["Category"] == "Geography")  | (df_cat["Category"] == "General Science")]
    plt.figure(figsize=(25,14)) 
    sns.lineplot(x="Publication Year", y="Count", hue="Category", data=df_cat_main)