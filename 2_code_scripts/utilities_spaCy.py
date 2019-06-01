#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:40:55 2019

@author: giudittaparolini
"""
import pandas as pd
import spacy
import os
import matplotlib.pylab as plt
from more_itertools import take
import utilities as ut
import json


nlp = spacy.load("en_core_web_sm")
nlp.Defaults.stop_words |= {"=","inch","+","°","p.","possible","cent","c"}


#Load each paper in spaCy using the paper id
def load_in_spacy(file_id):
    paper = ut.read_art_txt(file_id)
    my_doc = nlp(paper)
    return my_doc

#Generate list of tokens for each paper
def get_tokens(file_id):
    my_doc = load_in_spacy(file_id)
    my_tokens = []
    for my_token in my_doc:
        my_tokens.append(my_token)
    return my_tokens

#Remove punctuation, spaces, digits, new line character from tokens for each paper
def my_remove(file_id):
    _tokens = get_tokens(file_id)
    tokens_no_punct = []
    for my_token in _tokens:
        if my_token.is_punct == False:
            tokens_no_punct.append(my_token)    
    tokens_clean = []
    for tok in tokens_no_punct:
        if str(tok) != "\n":
            tokens_clean.append(tok)
    tokens_clean1 = []
    for mytok in tokens_clean:
        if mytok.is_space == False:
            tokens_clean1.append(mytok)       
    tokens_clean2 = []
    for myt in tokens_clean1:
        if myt.is_digit == False:
            tokens_clean2.append(myt)
    tokens_clean3 = []
    for mytk in tokens_clean2:
        if len(mytk) > 2:
            tokens_clean3.append(mytk)
    tokens_clean4 = []
    for mytkn in tokens_clean3:
        if "." not in mytkn:
            tokens_clean4.append(mytkn)       
    return tokens_clean4

#Generate list of lemmas for each paper
def get_lemmas(file_id):
    tokens_no_punct = my_remove(file_id)
    my_lemmas = []
    for token in tokens_no_punct:
        my_lemmas.append(token.lemma_)
    return my_lemmas

#Remove stopwords from my_lemmas for each paper
def remove_stopwords(file_id):
    stopwords = spacy.lang.en.stop_words.STOP_WORDS
    my_lemmas = get_lemmas(file_id)
    lemmas_clean = []
    for my_lemma in my_lemmas:
        if my_lemma not in stopwords:
            lemmas_clean.append(my_lemma)
    lemmas_clean_fin = []
    for my_lem in lemmas_clean:
        if my_lem != '-PRON-':
            lemmas_clean_fin.append(my_lem)
    return lemmas_clean_fin

#Count the occurrence of the lemmas in lemmas_clean
def count_lemma_freq(file_id):
    my_lemmas = remove_stopwords(file_id)
    lemma_counts = []
    for my_lemma in my_lemmas:
        count = my_lemmas.count(my_lemma)
        if [my_lemma, count] not in lemma_counts:
            lemma_counts.append([my_lemma, count])
            lemma_counts.sort(key = lambda x: x[1], reverse = True) 
    return lemma_counts

#Generate a dictionary of the lemmas counts for each paper
def get_lemmas_dict(file_id):
    my_lemma_counts = count_lemma_freq(file_id)
    lemmas_dict = { k[0]: k[1] for k in my_lemma_counts }
    return lemmas_dict

#Save the lemmas dictionary
def save_dict_spacy(file_id):
    my_dict = get_lemmas_dict(file_id)
    my_file_ext = "word_count_" + file_id + ".txt"
    with open(os.path.join("..", "3_printouts", "spaCy", my_file_ext), 'w') as outfile:  
        json.dump(my_dict, outfile, indent=4)

#Generate a plot of the common words (count > 5) in the lemmas dictionary
def plot_pop_words(file_id):
    my_file_ext = "word_count_" + file_id + ".txt"
    with open(os.path.join("..", "3_printouts", "spaCy", my_file_ext)) as json_file:  
        my_dict = json.load(json_file)
    plot_list = take(5, my_dict.items())
    x, y = zip(*plot_list)
    plt.figure(figsize=(14,8))
    df = pd.read_csv(os.path.join("..", "1_data", "full_data.csv"))
    paper_title = df[df['id']==file_id]['Title'].values
    plt.suptitle(str(paper_title), fontsize=10)
    plt.plot(x, y)

#Save the plot of the common words
def save_plot_spacy(file_id):
    fig = plot_pop_words(file_id)
    my_file_ext_p = file_id + ".pdf"
    plt.savefig(os.path.join("..", "4_plots", "spaCy_plots", my_file_ext_p))