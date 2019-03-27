#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:53:43 2019

@author: giudittaparolini
"""
import pandas as pd
import matplotlib.pyplot as plt
import csv
#import os
 

#tracks my path
#my_path = os.path.abspath(__file__)

# Language data (all)
df = pd.read_csv("language_counts.csv")

#I plot everything step by step to see if I am doing the right thing
print (df)


#I pair each language with its count in a list
with open("language_counts.csv", 'r') as f:
  reader = csv.reader(f)
  my_list = list(reader)

print(my_list)

#I now want to eliminate the first element of the list because it is the header and the couples with counts less or equal to 5
indexes = [0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
for index in sorted(indexes, reverse=True):
    del my_list[index]

#When I reprint the list I now have only the data I want (language-count). I can use my_list as a dictionary
print(my_list)

#I extract the language elements from my list for the pie chart
languages = dict(my_list).keys()
print (languages)

#Idem for the value counts
counts = dict(my_list).values()
print (counts)

#Now I can prepare the pie chart and legend
fig=plt.figure(figsize=(18,14))
plt.pie(counts, labels=languages,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Publications distributed according to language")
plt.legend()
plt.axis('equal')
#plt.savefig(my_path + "/4_plots/plot_language_count.png") wrong
plt.savefig("plot_language_count.png") #savefig must be called before show, otherwise fig is empty
#plt.savefig("/Users/giudittaparolini/OneDrive\ -\ Technische\ Universität\ Berlin/Coding/learn_it_girls/learn_IT_girls_python/4_plots/plot_language_count.png") not working
plt.show()




