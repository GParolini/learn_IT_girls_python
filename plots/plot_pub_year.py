#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:43:32 2019

@author: giudittaparolini
"""

import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('bibliography.csv', error_bad_lines=False)
df.columns = df.columns.str.strip()

fig=plt.figure(figsize=(17,10))
df.hist(column="Publication Year", bins=40 )
plt.xlabel("Publication Year",fontsize=15)
plt.ylabel("Frequency",fontsize=15)
plt.xlim([1900,1950])

fig=plt.figure(figsize=(17,10))
df.hist(column="Publication Year", bins=100 )
plt.xlabel("Publication Year",fontsize=15)
plt.ylabel("Frequency",fontsize=15)
plt.xlim([1900,1950])

fig=plt.figure(figsize=(17,10))
df.hist(column="Publication Year", bins=400 )
plt.xlabel("Publication Year",fontsize=15)
plt.ylabel("Frequency",fontsize=15)
plt.xlim([1900,1950])

fig=plt.figure(figsize=(17,10))
df.hist(column="Publication Year", bins=1000 )
plt.xlabel("Publication Year",fontsize=15)
plt.ylabel("Frequency",fontsize=15)
plt.xlim([1900,1950])

fig=plt.figure(figsize=(17,10))
df.hist(column="Publication Year", bins=1500 )
plt.xlabel("Publication Year",fontsize=15)
plt.ylabel("Frequency",fontsize=15)
plt.xlim([1900,1950])