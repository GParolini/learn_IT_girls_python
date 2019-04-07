#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:14:09 2019

@author: giudittaparolini
"""

#PLOT HIST LANGUAGES

import pandas as pd
import matplotlib as plt
import seaborn as sns
import os

#read data
df = pd.read_csv(os.path.join("..","..", "1_data","cleandata.csv"))

#set the background for the plot
sns.set(style="darkgrid")

#set plot size
sns.set(rc={'figure.figsize':(25,14)})

#create the plot
sns.countplot(y='Language', data=df)

#save the figure to a file in the folder 4_plots
#plt.savefig(os.path.join("..","..", "4_plots","plot_publ_language.png"))

#PLOT HIST PUB YEAR
#import pd and plt
import pandas as pd
from matplotlib import pyplot as plt
import os

#read data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#set histogram size
fig=plt.figure(figsize=(25,14))

#build the histogram with matplotlib
df.hist(column="Publication Year", bins=50 )

#set x and y labels
plt.xlabel("Publication Year",fontsize=15)
plt.ylabel("Frequency",fontsize=15)

#save the figure to a file in the folder 4_plots
plt.savefig(os.path.join("..","..", "4_plots","plot_publ_year.png"))

#PLOT PIE LANGUAGES
import matplotlib.pyplot as plt
import csv
import os

# Load data
#I pair each language with its count in a list
with open(os.path.join("..","..", "1_data","language_counts.csv")) as f:
  reader = csv.reader(f)
  my_list = list(reader)

#I now want to eliminate the first element of the list because it is the header
indexes = [0]
for index in sorted(indexes, reverse=True):
    del my_list[index]

#I extract the language elements from my list for the pie chart
languages = dict(my_list).keys()
print (languages)

#Idem for the value counts
counts = dict(my_list).values()
print (counts)

#Now I can prepare the pie chart and legend
fig=plt.figure(figsize=(10,8))
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(counts, explode,labels=None, 
autopct='%1.1f%%', pctdistance=1.1, shadow=True, startangle=140)
plt.title("Publications distributed according to language")
plt.legend(loc="best", labels=languages )
plt.axis('equal')


#save figure in file
plt.savefig(os.path.join("..","..", "4_plots","pie_language_count.png")) #savefig 


#PLOT PAIRS

import seaborn as sns
import os

#read data
df = sns.load_dataset(os.path.join("..","..", "1_data","cleandata.csv"))
