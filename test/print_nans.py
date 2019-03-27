#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""

import pandas as pd

df = pd.read_csv("cleandata.csv")

df.isna().sum().to_csv("nans.csv",mode='a')
