#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:00:59 2019

@author: giudittaparolini
"""

import pandas as pd
import seaborn as sns

df = pd.read_csv("cleandata.csv")

sns.countplot(y='Language', data=df)


