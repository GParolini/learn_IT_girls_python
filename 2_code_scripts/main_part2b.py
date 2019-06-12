#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""


import pandas as pd
import utilities_part1 as ut
import utilities_part2 as uts
import os
import matplotlib.pylab as plt
import spacy
import numpy as np

#Load spacy English model
nlp = spacy.load("en_core_web_sm")

# Read the ids of the English articles in the bibliography data
tit_ids = uts.get_eng_art_id()

#Generate a lemma dictionary for the title of each journal article
my_dicts = [uts.get_lemmas_tit_count_cat(file_id) for file_id in tit_ids] 

#Generate the global lemma dictionary joining the dictionaries for all the journal articles and saves it as a json file
uts.get_global_dict_titles(my_dicts)

#Counts the occurrence of the lemmas in each category and saves it in a json file
uts.get_global_dict_counts()
    
#Generate a dictionary where categories are keys and the counts of the given word in that category are given as percentages  
print("For the word water the resul is the following:" + uts.get_perc_counts_word("water"))

#Generate a list of unique lemmas across all categories
words = uts.get_all_words()

for word in words:
    my_res = uts.get_total_counts_word(word)
uts.print_txt_printouts (my_res, "total_word_counts")

print(uts.get_all_words()  ) 
    
print(uts.get_freq_words(50))
uts.plot_freq_words_title(20)
    
print(uts.get_total_counts_word_cat("plant", "Gardening"))
print(uts.get_freq_words_cat("Gardening", 5))
