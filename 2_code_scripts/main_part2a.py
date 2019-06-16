#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolin
"""
""" 
Main script for Part 2/a (text analysis of English journal articles(full papers)).
The text (txt file) of the articles is in 1_data/papers. Using methods in utilities_part2 the script reads the full text of all the articles (as string), count the length of the string, count the number of words. This information is merged with the original dataset (once cleaned, "clendata.csv").
The script also loads Spacy English Model, then loads the articles in Spacy and generates a lemma dictionary (saved in 3_printouts/part2/a) with counts for each article; plots the most frequent words for each article (saved in 4_plots/part2/a); using name-entity recognition extract geographical names for each article and saves them in 3_printouts/part2/a. Name-entity recognition of geographical names with the standard spacy model is not satisfactory with my dataset.
"""

import pandas as pd
import utilities_part1 as ut
import utilities_part2 as uts
import os
import matplotlib.pylab as plt
import spacy


# Read the ids of the txt files in the folder papers
file_ids = uts.read_art_id()

# Read the text of the files one by one and collect them in a dataframe adding the column id
d = []
for file_id in file_ids:
    file_txt = uts.read_art_txt(file_id)
    d.append([file_id, file_txt])

# Print the dataframe in a csv with column headers
papers = pd.DataFrame(d, columns=("id", "text"))
ut.print_csv_data_headers (papers, "papers.csv")

# Get the length of the txt file (as a string) and collect all the lengths in a dataframe 
d1 = []
for file_id in file_ids:
    file_length= uts.get_length_art_file(file_id)
    d1.append([file_id, file_length])

# Add the length column to the dataframe papers
length = pd.DataFrame(d1, columns=("id", "length"))
dfa = pd.merge(papers, length)
ut.print_csv_data_headers (dfa, "papers.csv")

# Get the word count of the txt file and collect all the word counts in a dataframe
d2 = []
for file_id in file_ids:
    file_word_count= uts.get_whitespaces_file(file_id)
    d2.append([file_id, file_word_count])

# Add the word count column to the dataframe papers
word_count = pd.DataFrame(d2, columns=("id", "word_count"))
dfb = pd.merge(dfa, word_count)
ut.print_csv_data_headers (dfb, "papers.csv")

#Right join of the dataframe papers with the bibliography data used in part 1 of the project
df = pd.read_csv(os.path.join("..", "1_data", "cleandata.csv"))
merged_p1_p2 = pd.merge(left=df,right=dfb, how="right", left_on="Key", right_on="id")
ut.print_csv_data (merged_p1_p2, "full_data.csv")

#Load spacy English model
nlp = spacy.load("en_core_web_sm")

#Generate dictionary
for file_id in file_ids:
    uts.get_lemmas_dict(file_id)
    continue

#Save dictionary
for file_id in file_ids:
    uts.save_dict_spacy(file_id)
    continue

#Plot the most frequent words for each paper and save them in 4_plots/part2
for file_id in file_ids:
    uts.plot_pop_words(file_id)
    plt.close()
    continue

#Print geographical names and save them in 3_printouts/part2/a
for file_id in file_ids:
    uts.print_geo_names(file_id)
    continue

