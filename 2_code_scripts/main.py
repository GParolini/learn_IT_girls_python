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
df = pd.read_csv(os.path.join("..", "1_data", "bibliography_data.csv"))

#List and print column headers
col_headers = df.columns.tolist()
ut.print_txt_printouts (col_headers, "column_headers.txt")

#Drop columns not necessary for data analysis
df1 =df.drop(["Date Added", "Date Modified", "Access Date"], axis=1)

#Eliminate the columns with more than 97 per cent NaNs and ensures that the entries in "Publication year" are integers not floats
df2 = dm.drop_nans_col(df1)
df3 = dm.colval_to_int(df2, "Publication Year")

#Print the cleaned data in a csv
ut.print_csv_data(df3, "cleandata.csv")

#Plot the histogram of the languages and save it in 4_plots
fig1 = pl.count_plot_lang(df)
ut.print_plot(fig1, "plot_publ_language.png")

#Plot the histogram of the publications per year and save it in 4_plots
fig2 = pl.hist_pub_year(df)
ut.print_plot(fig2, "plot_publ_year.png")

#Generate the language count txt file
lc = pr.lang_counts(df)
ut.print_csv_printouts (lc, "lang_counts.csv")

#Generate the pie chart of the language counts using the data in the txt file
fig3 = pl.pie_lang()
ut.print_plot(fig3, "plot_pie_languages.png")

