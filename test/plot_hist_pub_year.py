#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:00:59 2019

@author: giudittaparolini
"""
#import pd and plt
import pandas as pd
from matplotlib import pyplot as plt

#read clean data
df = pd.read_csv("cleandata.csv")

#set histogram size
fig=plt.figure(figsize=(25,14))

#build the histogram with matplotlib
df.hist(column="Publication Year", bins=50 )

#set x and y labels
plt.xlabel("Publication Year",fontsize=15)
plt.ylabel("Frequency",fontsize=15)

#save the figure to a file
plt.savefig("plot_language_count.png")