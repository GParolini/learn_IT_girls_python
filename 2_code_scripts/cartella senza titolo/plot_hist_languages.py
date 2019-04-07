#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:00:59 2019

@author: giudittaparolini
"""

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