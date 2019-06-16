#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""
""" 
Main script for Part 2/b (text analysis of the titles for all the English journal articles).
The script generates a global dictionary of lemmas (with counts) for each category. The final dictionary is saved as a json file in 3_printouts/part2/b. All the methods used by this main script are in utilities_part2.
"""

import utilities_part2 as uts
import spacy

#Load spacy English model
nlp = spacy.load("en_core_web_sm")

# Read the ids of the English articles in the bibliography data
tit_ids = uts.get_eng_art_id()


#for file_id in tit_ids:
    #print(uts.get_eng_art_lemmas_tit_count_cat(file_id))

#Generate a dictionary with lemmas for each journal article
my_dicts = [uts.get_eng_art_lemmas_tit_count_cat(file_id) for file_id in tit_ids] 

#Generate a global lemma dictionary for all the English journal articles and saves it as a json file
uts.get_eng_art_global_lemmas_dict(my_dicts)

#Generate a global dictionary that has counts for each lemma in each category
uts.get_eng_art_global_dict_with_counts()
    
