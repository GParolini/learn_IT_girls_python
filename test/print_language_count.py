#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:53:03 2019

@author: giudittaparolini
"""

import pandas as pd

df = pd.read_csv("cleandata.csv")

lan_counts = df["Language"].value_counts()

lan_counts.to_csv("language_counts.csv", mode = "a", header=["Count"])