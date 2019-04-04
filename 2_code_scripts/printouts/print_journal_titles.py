#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:37:36 2019

@author: giudittaparolini
"""

import pandas as pd
import os

#read data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#list itemtypes labels in the data
item_types =list(set(df["Item Type"]))

print(item_types)

journal_articles = df.loc[df['Item Type'] == 'journalArticle']

journal_titles = journal_articles["Publication Title"].dropna()

journal_titles_unique = list(set(journal_titles))

journal_titles_unique.sort()


with open(os.path.join("..","..", "3_printouts", "journal_titles.txt"), 'w') as outfile:
    for title in journal_titles_unique:
        print(title, file=outfile)