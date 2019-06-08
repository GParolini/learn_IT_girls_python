#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""


import pandas as pd
import utilities as ut
import utilities_spaCy as uts
import os
import matplotlib.pylab as plt


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

#Right join of the dataframe papers with the bibliography data used in part 1 of the project
df = pd.read_csv(os.path.join("..", "1_data", "cleandata.csv"))
merged_p1_p2 = pd.merge(left=df,right=dfb, how="right", left_on="Key", right_on="id")
ut.print_csv_data (merged_p1_p2, "full_data.csv")

#Plot the most frequent words for each paper
#for file_id in file_ids:
    #uts.plot_pop_words(file_id)
    #continue
    #plt.close()

#Save frequent words plots
#for file_id in file_ids:
    #uts.save_plot_spacy(file_id)
    #continue   

tit_ids = uts.get_eng_art_id()

#for file_id in tit_ids:
    #print(uts.get_lemmas_tit_count(file_id))

#my_dicts = [uts.get_lemmas_tit_count_cat(file_id) for file_id in tit_ids] 
                
#uts.get_global_dict_titles(my_dicts)

#uts.get_global_dict_counts()
    
#uts.get_matrix_dict_counts()
    
#print(uts.get_perc_counts_word("water"))

#uts.get_perc_counts_word()
word_counts = uts.get_freq_words()
#print(word_counts)

#print (type(word_counts))

#uts.get_most_freq_words(word_counts)
