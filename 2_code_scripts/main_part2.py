#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""



import print_methods as pr
import utilities as ut




# Read the txt files in the folder papers as strings
df = ut.read_art_txt()
ut.print_txt_printouts (df, "papers.txt")

# Get the length of each string
my_lengths = pr.get_length_art(df)
ut.print_txt_printouts (my_lengths, "lengths.txt")

#Get the number of words in each file
word_count = pr.get_whitespaces(df)
ut.print_txt_printouts (word_count, "word_counts.txt")

#test case with a simple string
my_str = ut.read_art_txt_file("test.txt")

print (ut.read_art_txt_file("test.txt"))

print (pr.get_length_art_file(my_str))

print (pr.get_whitespaces_file(my_str))

