#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:14:09 2019

@author: giudittaparolini
"""
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import os

#PLOT HIST LANGUAGES
def count_plot_lang(df):
     sns.set(style="darkgrid")
     sns.set(rc={"figure.figsize":(25,14)})
     sns.countplot(y="Language", data=df)
     
#PLOT HIST OF THE PUBLICATION YEARS
def hist_pub_year(df):
    plt.figure(figsize=(25,14))
    df.hist(column="Publication Year", bins=50 )
    plt.xlabel("Publication Year",fontsize=15)
    plt.ylabel("Frequency",fontsize=15)

#PLOT PIE CHART LANGUAGES
def lang_count_list():
    with open(os.path.join("..", "3_printouts","lang_counts.csv")) as f:
        reader = csv.reader(f)
        my_list = list(reader)
    return my_list
        
def pie_lang():
    my_list = lang_count_list()
    languages = dict(my_list).keys()
    counts = dict(my_list).values()
    plt.figure(figsize=(10,8))      
    explode = (0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    plt.pie(counts, explode,labels=None, 
            autopct='%1.1f%%', pctdistance=1.1, shadow=True, startangle=140)
    plt.title("Publications distributed according to language")
    plt.legend(loc="best", labels=languages )
    plt.axis('equal')







#PLOT PAIRS





#PLOT PAIRS

#import seaborn as sns
#import os

#read data
#df = sns.load_dataset(os.path.join("..","..", "1_data","cleandata.csv"))
