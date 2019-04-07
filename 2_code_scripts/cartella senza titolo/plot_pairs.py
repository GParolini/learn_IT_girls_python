#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:49:28 2019

@author: giudittaparolini
"""




import seaborn as sns
import os

#read data
df = sns.load_dataset(os.path.join("..","..", "1_data","cleandata.csv"))
