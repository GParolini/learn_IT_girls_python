#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""

import pandas as pd

df = pd.read_csv("bibliography_data_24_march.csv")
df.columns = df.columns.str.strip()