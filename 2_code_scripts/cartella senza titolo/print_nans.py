#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""

import pandas as pd
import os

#read the data
df = pd.read_csv(os.path.join("..","..", "1_data", "bibliography_data.csv"))


df.isna().sum().to_csv(os.path.join("..","..", "3_printouts", "nans.csv"), mode = "a")
