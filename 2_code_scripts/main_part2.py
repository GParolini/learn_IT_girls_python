#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""

import pandas as pd
import os
import data_methods as dm
import print_methods as pr
import plot_methods as pl
import utilities as ut




#Load the data
df = ut.read_art_txt()
ut.print_txt_printouts (df, "papers.txt")

my_lengths = pr.get_length_art(df)
ut.print_txt_printouts (my_lengths, "lengths.txt")

word_count = pr.get_whitespaces(df)
ut.print_txt_printouts (word_count, "word_counts.txt")

my_str = ut.read_art_txt_file("test.txt")

print (ut.read_art_txt_file("test.txt"))

print (pr.get_length_art_file(my_str))
