#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""


import pandas as pd
import utilities as ut


# Read the ids of the txt files in the folder papers
file_ids = ut.read_art_id()


# Read the text of the files one by one and collect them in a dataframe adding the column id
d = []
for file_id in file_ids:
    file_txt = ut.read_art_txt(file_id)
    d.append([file_id, file_txt])


# Print the dataframe in a csv with column headers
papers = pd.DataFrame(d, columns=("id", "text"))
ut.print_csv_data_headers (papers, "papers.csv")

# Get the length of the txt file (as a string) and collect all the lengths in a dataframe 
d1 = []
for file_id in file_ids:
    file_length= ut.get_length_art_file(file_id)
    d1.append([file_id, file_length])

# Add the length column to the dataframe papers
length = pd.DataFrame(d1, columns=("id", "length"))
dfa = pd.merge(papers, length)
ut.print_csv_data_headers (dfa, "papers.csv")

# Get the word count of the txt file and collect all the word counts in a dataframe
d2 = []
for file_id in file_ids:
    file_word_count= ut.get_whitespaces_file(file_id)
    d2.append([file_id, file_word_count])

# Add the word count column to the dataframe papers
word_count = pd.DataFrame(d2, columns=("id", "word_count"))
dfb = pd.merge(dfa, word_count)
ut.print_csv_data_headers (dfb, "papers.csv")
