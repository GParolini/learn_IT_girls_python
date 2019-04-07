#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:53:43 2019

@author: giudittaparolini
"""

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





