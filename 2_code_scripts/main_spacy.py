#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 00:13:56 2019

@author: giudittaparolini
"""

import utilities as ut
import utilities_spaCy as uts
import spacy


nlp = spacy.load("en_core_web_sm")

#Get the file ids
spacy_ids = ut.read_art_id()

#Get tokens
#for file_id in spacy_ids:
    #uts.get_tokens(file_id)

#Get lemmas
#for file_id in spacy_ids:
    #uts.get_lemmas(file_id)

#Remove punctuation
#for file_id in spacy_ids:
    #uts.my_remove(file_id)

#Get lemmas
#for file_id in spacy_ids:
    #uts.get_lemmas(file_id)

#Remove stopwords
#for file_id in spacy_ids:
    #uts.remove_stopwords(file_id)

#Count frequency
#for file_id in spacy_ids:
    #uts.count_lemma_freq(file_id)
    #continue

#Generate dictionary
for file_id in spacy_ids:
    uts.get_lemmas_dict(file_id)
    continue

#Save dictionary
for file_id in spacy_ids:
    uts.save_dict_spacy(file_id)
    continue

#Get geographical names
for file_id in spacy_ids:
    uts.get_places(file_id)
    continue
    

