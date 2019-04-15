#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:14:09 2019

@author: giudittaparolini
"""

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
