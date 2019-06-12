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
import glob
import re
import itertools
from more_itertools import take
import utilities_part1 as ut
import json
from collections import defaultdict
from collections import Counter
from operator import itemgetter
import numpy as np
from numpy import * 


nlp = spacy.load("en_core_web_sm")
nlp.Defaults.stop_words |= {"=","inch","+","°","p.","possible","cent","c"}


##########################
# Methods for reading text files, get their length (as string), count the number of words

#Read the id of all the txt files in a folder
def read_art_id():
    all_files = glob.glob("../1_data/papers/*.txt")
    files_ids = []
    for my_file in all_files:
            filename = os.path.basename(my_file)
            file_id = os.path.splitext(filename)[0]
            files_ids.append(file_id)
            continue
    return (files_ids)

#Read a single txt file using the file id    
def read_art_txt(file_id):
    file_ext = file_id + ".txt"
    with open (os.path.join("..", "1_data","papers", file_ext), "rt") as f: 
            text = f.read()
    return (text)

#Count the length of a txt file
def get_length_art_file(file_id):
    file_txt = read_art_txt(file_id)
    length = len(file_txt) - 1
    return length  

#Get words in a txt file (by counting white spaces)
def get_whitespaces_file(file_id):
    file_txt = read_art_txt(file_id)
    word_count = len(re.findall(r' +', file_txt))
    final_word_count = word_count + 1
    return final_word_count


##########################
# Methods for loading the full text of the extracted papers into spacy, getting tokens and lemmas, cleaning them, remove stopwords, count the occurrence of lemmas, generate a plot of the most common lemmas and save them, use name-entity recognition to individuate geographical names


#Load each paper in spaCy using the paper id
def load_in_spacy(file_id):
    paper = read_art_txt(file_id)
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
    return tokens_clean3

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
    my_file_ext = "word_count_" + file_id + ".json"
    with open(os.path.join("..", "3_printouts", "part2", my_file_ext), 'w') as outfile:  
        json.dump(my_dict, outfile, indent=4)

#Generate a plot of the common words (count > 5) in the lemmas dictionary
def plot_pop_words(file_id):
    my_file_ext = "word_count_" + file_id + ".json"
    with open(os.path.join("..", "3_printouts", "part2", my_file_ext)) as json_file:  
        my_dict = json.load(json_file)
    plot_list = {k: my_dict[k] for k in list(my_dict.keys())[:5]}
    plt.bar(range(len(plot_list)), list(plot_list.values()), align='center')
    plt.xticks(range(len(plot_list)), list(plot_list.keys()))
    plt.figure(figsize=(14,8))
    df = pd.read_csv(os.path.join("..", "1_data", "full_data.csv"))
    paper_title = df[df['id']==file_id]['Title'].values
    plt.suptitle(str(paper_title), fontsize=10)
    plt.close()
    

#Save the plot of the common words
def save_plot_spacy(file_id):
    fig = plot_pop_words(file_id)
    my_file_ext_p = file_id + ".pdf"
    plt.savefig(os.path.join("..", "4_plots", "part2", my_file_ext_p))

#Get geographical names
def get_places(file_id):
    paper = read_art_txt(file_id)
    my_doc = nlp(paper)
    #entities = []
    for ent in my_doc.ents:
        if ent.label_ == 'GPE':
            print(ent.text)

##########################
# Methods for working with the title of the English articles in the bibliography data, associate it with the article category, count the most frequent lemmas across all categories and a in a specific category and plot them


#Get all the journal articles in English from the original data
def get_eng_art_id():
    df = pd.read_csv(os.path.join("..", "1_data", "df_jour_cat.csv"))
    df_not_eng = df[df["Language"] != "English"]
    df_eng = df.drop(df_not_eng.index, axis = 0)
    file_ids = df_eng["Key"]
    return file_ids

#Gets the category corresponding to the file_id
def get_eng_art_cat(file_id):
    df = pd.read_csv(os.path.join("..", "1_data", "df_jour_cat.csv"))
    cat = df[df["Key"] == file_id]['Category'].values
    my_cat = ''.join([str(elem) for elem in cat])
    return my_cat

#Gets the title corresponding to the file_id
def get_eng_art_title(file_id):
    df = pd.read_csv(os.path.join("..", "1_data", "df_jour_cat.csv"))
    title = df[df["Key"] == file_id]['Title'].values
    my_title = ''.join([str(elem) for elem in title])
    return my_title

#Reads the title corresponding to the file_id in spacy
def read_eng_tit_spacy(file_id):
    my_title = get_eng_art_title(file_id)
    my_doc = nlp(my_title)
    return my_doc

#Get the tokes for the title corresponding to the file_id
def get_eng_tit_tok(file_id):
    my_doc = read_eng_tit_spacy(file_id)
    my_tokens = []
    for my_token in my_doc:
        my_tokens.append(my_token)
    return my_tokens

#Clean the title tokens removing punctuations, new lines, spaces, digits, short words
def get_eng_tit_tok_clean(file_id):
    my_tokens = get_eng_tit_tok(file_id)
    tokens_no_punct = []
    for my_token in my_tokens:
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
    return tokens_clean3
  
#Get the lemmas in the title of a file after removing stopwords and pronouns    
def get_lemmas_tit(file_id): 
    my_tokens = get_eng_tit_tok_clean(file_id)
    my_lemmas = []
    for token in my_tokens:
        my_lemmas.append(token.lemma_)
    stopwords = spacy.lang.en.stop_words.STOP_WORDS
    lemmas_clean = []
    for my_lemma in my_lemmas:
        if my_lemma not in stopwords:
            lemmas_clean.append(my_lemma)
    lemmas_clean_fin = []
    for my_lem in lemmas_clean:
        if my_lem != '-PRON-':
            lemmas_clean_fin.append(my_lem)
    return lemmas_clean_fin

#Count the occurrence of lemmas in the title of a file
def get_lemmas_tit_count(file_id): 
    my_lemmas = get_lemmas_tit(file_id)
    lemma_counts = []
    for my_lemma in my_lemmas:
        count = my_lemmas.count(my_lemma)
        if [my_lemma, count] not in lemma_counts:
            lemma_counts.append([my_lemma, count])
            lemma_counts.sort(key = lambda x: x[1], reverse = True) 
    return lemma_counts

#Counts the occurrence of the lemmas in each category
def get_lemmas_tit_count_cat(file_id): 
    df = pd.read_csv(os.path.join("..", "3_printouts", "part1", "jourcat_counts.csv"), names=["Category", "Count"])
    my_dict = {}
    my_cat = df["Category"].values
    for cat in my_cat:
        my_dict.update( {cat : []} )
    my_lemmas = get_lemmas_tit(file_id)
    art_cat = str(get_eng_art_cat(file_id))
    for my_lemma in my_lemmas:
        my_dict[art_cat].append(my_lemma)
    return my_dict

#Counts the occurrence of the lemmas in each category and saves it in a json file       
def get_global_dict_titles(my_dicts):    
    dd = defaultdict(list)
    for d in my_dicts:
        for key, value in d.items():
            if value != []:
                for item in value:
                    dd[key].append(item)
    my_file_ext = "titles_dict" + ".json"
    with open(os.path.join("..", "3_printouts", "part2", my_file_ext), 'w') as outfile:  
        json.dump(dd, outfile, indent = 2, separators=(',', ': '))
    return dd

#Counts the occurrence of the lemmas in each category and saves it in a json file
def get_global_dict_counts():
    with open(os.path.join("..", "3_printouts", "part2", "titles_dict.json")) as json_file:  
        my_dict = json.load(json_file)
    my_keys = my_dict.keys()
    big_dict = {}
    for key in my_keys:
        my_counts = Counter(my_dict[key])
        big_dict.update( {key : my_counts} )
    my_file_ext = "count_dict" + ".json"
    with open(os.path.join("..", "3_printouts", "part2", my_file_ext), 'w') as outfile:  
        json.dump(big_dict, outfile, indent = 2, separators=(',', ': '))
    return big_dict

#Generate a dictionary where categories are keys and the counts of the given word in that category are given as percentages
def get_perc_counts_word(my_word):
    with open(os.path.join("..", "3_printouts", "part2", "count_dict.json")) as json_file:  
        big_dict = json.load(json_file)
    tot = {}
    for key in big_dict.keys():
        if my_word in big_dict[key]:
                tot.update({key : big_dict[key][my_word]})
        else:
            continue
    my_sum_list =[]
    for key in tot.keys():
        my_sum_list.append(tot[key])
    my_sum = sum(my_sum_list)
    tot_norm = {}
    for key in tot.keys():
        norm = tot[key]/my_sum
        per_cent = norm * 100
        norm_r = round(per_cent, 3)
        tot_norm.update({key : norm_r})
    return tot_norm

#Generate a list of unique lemmas across all categories
def get_all_words():
    with open(os.path.join("..", "3_printouts", "part2", "count_dict.json")) as json_file:  
        big_dict = json.load(json_file)
    word_list_cat = []
    for key in big_dict.keys():
        for my_word in big_dict[key]:
            if my_word not in word_list_cat:
                word_list_cat.append(my_word)
            else:
                continue
    return word_list_cat

#Get the counts (as integer) for a given word across all categories
def get_total_counts_word(my_word):
    with open(os.path.join("..", "3_printouts", "part2", "count_dict.json")) as json_file:  
        big_dict = json.load(json_file)
    tot = {}
    for key in big_dict.keys():
        if my_word in big_dict[key]:
                tot.update({key : big_dict[key][my_word]})
        else:
            continue
    my_sum_list =[]
    for key in tot.keys():
        my_sum_list.append(tot[key])
    my_sum = sum(my_sum_list)
    return (my_word, my_sum)

#Get the counts (as integer and as per cent of all the words in the category) for a given word and a given category
def get_total_counts_word_cat(my_word, my_cat):
    with open(os.path.join("..", "3_printouts", "part2", "count_dict.json")) as json_file:  
        big_dict = json.load(json_file)
        if my_word in big_dict[my_cat]:
                my_count = big_dict[my_cat][my_word]
    my_sum_list =[]
    for any_word in big_dict[my_cat]:
        my_sum_list.append(big_dict[my_cat][any_word])
    my_sum = sum(my_sum_list)
    my_percent = my_count/my_sum
    rounded = round(my_percent, 3)
    return (my_cat, my_word, my_count, rounded)
        
#Generate a dictionary of the most frequent words across all categories. The value num allows to select the required interval as a threshold on the number of counts
def get_freq_words(num):
    word_list = get_all_words()
    frequent_words =[]
    for word in word_list:
        count = get_total_counts_word(word)
        if count[1] >= num:
            frequent_words.append([word, count[1]])
    l = len(frequent_words) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (frequent_words[j][1] < frequent_words[j + 1][1]): 
                tempo = frequent_words[j] 
                frequent_words[j]= frequent_words[j + 1] 
                frequent_words[j + 1]= tempo
    frequent_dict = { k[0]: k[1] for k in frequent_words }
    return frequent_dict

#Generate a bar plot of the most frequent words across all categories
def plot_freq_words_title(num):
    my_dict = get_freq_words(num)
    plot_list = my_dict.items()
    x, y = zip(*plot_list)
    plt.figure(figsize=(14,20))
    plt.barh(x, y)


#Get the most frequent words for a specific category and a set threshold (num)
def get_freq_words_cat(my_cat, my_num):
    with open(os.path.join("..", "3_printouts", "part2", "count_dict.json")) as json_file:  
        big_dict = json.load(json_file)
    word_list_cat = []
    for any_word in big_dict[my_cat]:
        if any_word not in word_list_cat:
            word_list_cat.append(any_word)
    frequent_words = []
    for my_word in word_list_cat:
        my_count = big_dict[my_cat][my_word]
        frequent_words.append([my_word, my_count])
    l = len(frequent_words) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (frequent_words[j][1] < frequent_words[j + 1][1]): 
                tempo = frequent_words[j] 
                frequent_words[j]= frequent_words[j + 1] 
                frequent_words[j + 1]= tempo
    print(frequent_words)
    top_num = frequent_words[: my_num]
    frequent_cat_dict = { k[0]: k[1] for k in top_num }
    return frequent_cat_dict

#Generate a bar plot of the most frequent words in a specific category
def plot_cat_freq_words_title(my_cat, my_num):
    my_dict = get_freq_words_cat(my_cat, my_num)
    plot_list = my_dict.items()
    x, y = zip(*plot_list)
    plt.figure(figsize=(14,20))
    plt.barh(x, y)

#Print to a txt file in the folder 3_printouts/part_2
def print_txt_printouts (to_be_printed, filename):
    with open(os.path.join("..", "3_printouts","part2", filename),'w') as outfile:
        for item in to_be_printed:
            print(item, file=outfile)








    