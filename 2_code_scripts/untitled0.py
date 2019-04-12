#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:39:47 2019

@author: giudittaparolini
"""
import os
import csv
import itertools

def lang_count_list():
    with open(os.path.join("..", "3_printouts","lang_counts.csv")) as f:
        reader = csv.reader(f)
        my_list = list(reader)
        return my_list
    
print(lang_count_list())

def main_lang_list():
    with open(os.path.join("..", "3_printouts","lang_counts.csv")) as f:
        reader = csv.reader(f)
        my_list = list(reader)
    my_list = lang_count_list()
    agg_list = []
    for item in my_list[0:5]:
        agg_list.append(item)
    return agg_list

print(main_lang_list())

def other_count():
    my_list = lang_count_list()
    other_list = my_list[5:]
    other_list = list(itertools.chain(*other_list))
    other_count_list = other_list[1::2]
    other_count = [ int(x) for x in other_count_list ] 
    others = sum(other_count)
    return others

print(other_count())

def agg_list():
    agg_list = []
    main_lang = main_lang_list()
    for item in main_lang:
        agg_list.append(item)
    others = str(other_count())
    other_element = [["Other", others]]
    for item in other_element:
        agg_list.append(item)
    return agg_list

print(agg_list())

