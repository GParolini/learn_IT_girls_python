#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:40:55 2019

@author: giudittaparolini
"""
import pandas as pd
import spacy
import glob
import os
import pickle
import matplotlib.pylab as plt
from more_itertools import take


nlp = spacy.load("en_core_web_sm")
nlp.Defaults.stop_words |= {"=","inch","+","°","p.","possible","cent","c"}

#Get the id of all the txt files for the analysis with spaCy 
def get_spacy_id():
    all_files = glob.glob("*.txt")
    files_ids = []
    for my_file in all_files:
            filename = os.path.basename(my_file)
            file_id = os.path.splitext(filename)[0]
            files_ids.append(file_id)     
            continue
    return files_ids

#Read the txt files in the code folder
def read_spacy_txt(file_id):
    file_ext = file_id + ".txt"
    with open (file_ext, "rt") as f: 
            text = f.read()        
    return text

#Load each paper in spaCy using the paper id
def load_in_spacy(file_id):
    paper = read_spacy_txt(file_id)
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
    return tokens_clean2

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
        if [my_lemma,count] not in lemma_counts:
            lemma_counts.append([my_lemma,count])
            lemma_counts.sort(key = lambda x: x[1], reverse = True) 
    return lemma_counts

#Generate a dictionary of the lemmas counts for each paper
def get_lemmas_dict(file_id):
    my_lemma_counts = count_lemma_freq(file_id)
    lemmas_dict = { k[0]: k[1:] for k in my_lemma_counts }
    return lemmas_dict

#Save the lemmas dictionary
def save_dict_spacy(file_id):
    my_dict = get_lemmas_dict(file_id)
    my_file_ext = file_id + ".pickle"
    pickle_out = open(os.path.join("..", "3_printouts", "spaCy", my_file_ext),"wb")
    pickle.dump(my_dict, pickle_out)
    pickle_out.close()

#Print the lemmas dictionary
def print_lemma_dict(file_id):
    my_file_ext = file_id + ".pickle"
    pickle_in = open(os.path.join("..", "3_printouts", "spaCy", my_file_ext),"rb")
    my_dict = pickle.load(pickle_in)
    my_keys = my_dict.keys()
    my_file_ext1 = "dict_" + file_id + ".txt"
    with open(os.path.join("..", "3_printouts", "spaCy", my_file_ext1),'w') as outfile:
        for key in my_keys:
            print (key + ": ", my_dict[key], file=outfile)

#Generate a plot of the common words (count > 5) in the lemmas dictionary
def plot_pop_words(file_id):
    my_file_ext = file_id + ".pickle"
    pickle_in = open(os.path.join("..", "3_printouts", "spaCy", my_file_ext),"rb")
    my_dict = pickle.load(pickle_in)
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