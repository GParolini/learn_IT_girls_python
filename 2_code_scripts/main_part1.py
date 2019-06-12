#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""

""" 
Main script for Part 1.
The data in the bibliography are pre-processed using the data_methods and a clean dataset is generated (cleandata.csv).
To inspect the data, lists of item types (e.g. book, report) and counts are generated.
The code generates lists/plots of item titles for each item type, authors (both tuples of co-authors and a sorted list with all the individual author names), number of publications for each author, counts of the publication language, co-authorship groups, associations between journal and categories through a list provided in 1_data, publications per category per year, etc. The methods for generating printouts and plots are in print_methods_part1 and plot_methods_part1.
All the printouts are in 3_printouts/part1 (except the csv where the clean dataset restricted to journals is associated with the journal category, which is in 1_data), all the plots in 4_plots/part1.
"""




import pandas as pd
import os
import data_methods_part1 as dm
import print_methods_part1 as pr
import plot_methods_part1 as pl
import utilities_part1 as ut



#Load the data
df = pd.read_csv(os.path.join("..", "1_data", "bibliography_data.csv"))

#Load the categories data
df_cat = pd.read_csv(os.path.join("..", "1_data", "corr_journ_cat.csv"))

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

#Generate a list of the item types and print it in a txt file
item_types =list(set(df["Item Type"]))
ut.print_txt_printouts (item_types, "item_types.txt")

#Generate the item type count csv file
lc = pr.itemtype_counts(df3)
ut.print_csv_printouts (lc, "itemtype_counts.csv")

#Generate a list of the report titles and print them in a txt file
report_titles = pr.get_report_titles(df3)
ut.print_txt_printouts (report_titles, "report_titles.txt")

#Generate a list of the thesis titles and print them in a txt file
thesis_titles = pr.get_thesis_titles(df3)
ut.print_txt_printouts (thesis_titles, "thesis_titles.txt")

#Generate a list of the book titles and print them in a txt file
book_titles = pr.get_book_titles(df3)
ut.print_txt_printouts (book_titles, "book_titles.txt")

#Generate a list of the journal titles and print them in a txt file
journal_titles = pr.get_journal_titles(df3)
ut.print_txt_printouts (journal_titles, "journal_titles.txt")

#Generate a count of the articles in each journal and print them in a csv file
articles_per_journal = pr.get_art_count_per_journal(df3)
ut.print_csv_printouts (articles_per_journal, "articles_per_journal.csv")

#Generate a list of the magazine titles and print them in a txt file
magazine_titles = pr.get_magazine_titles(df3)
ut.print_txt_printouts (magazine_titles, "magazine_titles.txt")

#Generate a list of the newspaper titles and print them in a txt file
newspaper_titles = pr.get_newspaper_titles(df3)
ut.print_txt_printouts (newspaper_titles, "newspaper_titles.txt")

#Generate a list of the first authors and print them in a txt file
first_authors = pr.get_first_authors(df3)
ut.print_txt_printouts (first_authors, "first_authors.txt")

#Generate the author count csv file
lc = pr.author_counts(df3)
ut.print_csv_printouts (lc, "author_counts.csv")

#Generate a list of all the authors and print them in a txt file
all_authors = pr.get_all_authors(df3)
ut.print_txt_printouts (all_authors, "all_authors.txt")

#Generate a list of the multi-authors and print them in a txt file
first_authors = list(pr.get_first_authors(df3))
multi_authors = pr.get_multiauthors(first_authors)
ut.print_txt_printouts (multi_authors, "multiauthors.txt")

#Generate a list of the co-authors nested and print them in a txt file
multi_authors_list = list(multi_authors)
all_authors_list = list(all_authors)
co_authors_nested = pr.get_coauthors_nested(multi_authors_list, all_authors_list)
authors = pr.get_pop_author(co_authors_nested)
ut.print_txt_printouts (co_authors_nested, "coauthors_nested.txt")

#Generate a list of the co-authors and print them in a txt file
co_authors_pop = pr.get_coauthors_pop(co_authors_nested)
ut.print_txt_printouts (co_authors_pop, "coauthors_pop.txt")

#Generate a dictionary of the co-authors 
co_authors_flat = pr.get_coauthors_flatten(co_authors_pop)
co_authors_unique = pr.get_coauthors_unique (co_authors_flat)
coauthors_dict = pr.get_dict_coauthors(authors,co_authors_unique)
coauthors_dict_clean = pr.get_dict_clean(coauthors_dict)
ut.save_dict(coauthors_dict_clean)
ut.print_coaut_dict("coauthors_dict.pickle", "my_coauthors.txt")

#Plot the histogram of the publications per year and save it in 4_plots
fig2 = pl.hist_pub_year(df)
ut.print_plot(fig2, "plot_publ_year.png")

#Plot the histogram of the languages and save it in 4_plots
fig1 = pl.count_plot_lang(df)
ut.print_plot(fig1, "plot_publ_language.png")

#Generate the language count csv file
lc = pr.lang_counts(df3)
ut.print_csv_printouts (lc, "lang_counts.csv")

#Generate the pie chart of the language counts using the data in the csv file
fig3 = pl.pie_lang()
ut.print_plot(fig3, "plot_pie_languages.png")

#Generate the journal categories count csv file
df_jcat = ut.get_journal_cat(df3,df_cat)
jourcat = pr.jourcat_counts(df_jcat)
ut.print_csv_printouts (jourcat, "jourcat_counts.csv")

#Generate the correspondence journal-categories and print the resulting df in a csv file
journal_cat = ut.get_journal_cat(df,df_cat)
ut.print_csv_data (journal_cat, "df_jour_cat.csv")

#Generate the count of the journal articles in each category and in each year and print it in a csv file
df_jcat = ut.get_journal_cat(df3,df_cat)
jourcat_year = pr.jourcat_year_counts(df_jcat)
#df_headers = pd.DataFrame(jourcat_year, columns = ["Category", "Publication Year", "Count"])
ut.print_csv_printouts (jourcat_year, "jourcat_year_counts.csv")

#Generate the pie chart of the journal category counts using the data in the csv file
fig4 = pl.pie_jcat()
ut.print_plot(fig4, "plot_pie_jcat.png")

#Generate the scatter plot of the categories/year count
fig5 = pl.scatter_jcat()
ut.print_plot(fig5, "plot_scatter_jcat.png")

#Generate the scatter plot of the categories/year count only for 1920 to 1940
fig6 = pl.scatter_jcat_l()
ut.print_plot(fig6, "plot_scatter_jcat_l.png")

#Generate the scatter plot group of the categories/year count for 1925, 1930, 1935
fig7 = pl.scatter_grouped()
ut.print_plot(fig7, "plot_scatter_grouped.png")

#Generate the scatter plot group of the categories/year count for 1925, 1930 and 1935
fig8 = pl.scatter_grouped_lg()
ut.print_plot(fig8, "plot_scatter_grouped_lg.png")

#Generate the line plot group of the categories/year count
fig9 = pl.line_jcat()
ut.print_plot(fig9, "plot_line_jcat.png")

#Generate the line plot group of the main categories/year count
fig10 = pl.line_jcat_main()
ut.print_plot(fig10, "plot_line_jcat_main.png")