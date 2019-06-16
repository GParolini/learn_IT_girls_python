#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:57:54 2019

@author: giudittaparolini
"""
""" 
Main script for Part 2/c (data mining of the global lemmas dictionary generated in Part 2/b).
The script calls methods for generating a list of unique lemmas across all categories, get counts and percentages for specific lemmas, generate dictionarries of the most common lemmas in a specific category and across all categories, and print the related plots. All the printouts are in 3_printouts/part2/c, the plots in 4_plots/part2/c. All the methods used by this main script are in utilities_part2.
"""



import utilities_part2 as uts


#Generate a list of unique lemmas across all categories and print it in a txt file in 3_printouts/part2
unique_lemmas = uts.get_all_lemmas_list()
uts.print_txt_printouts (unique_lemmas, "unique_lemmas.txt")

#Example of how to use the method get_counts_lemma(my_word). Results are saved in 3_printouts/part2
uts.get_counts_lemma("temperature")
uts.get_counts_lemma("plant")
uts.get_counts_lemma("hello")

#Example of how to use the method get_perc_counts_lemma(my_word). Results are saved in 3_printouts/part2
uts.get_perc_counts_lemma("temperature")
uts.get_perc_counts_lemma("plant")
uts.get_perc_counts_lemma("hello")

#Example of how to use the method get_both_counts_lemma_cat(my_word, my_cat). The result is printed in a txt file in 3_printouts/part2
my_example = [
uts.get_both_counts_lemma_cat("temperature", "Agriculture"),
uts.get_both_counts_lemma_cat("temperature", "Meteorology"),
uts.get_both_counts_lemma_cat("plant", "Agriculture"),
uts.get_both_counts_lemma_cat("plant", "Meteorology"),
uts.get_both_counts_lemma_cat("hello", "Agriculture"),
uts.get_both_counts_lemma_cat("hello", "Meteorology")
]
uts.print_txt_printouts (my_example, "my_example.txt")

#Generate a dictionary with all the lemmas whose count is higher or equal to a given number. Save the result in a json file in 3_printouts/part2
uts.get_freq_lemmas(100)
uts.get_freq_lemmas(50)

#Generate the plots corresponding to the above example. The plots are stored in 4_plots/part2
uts.plot_freq_lemmas_title(100)
uts.plot_freq_lemmas_title(50)

#Example of how to get the first 5 popular words in a category. The resulting dictionaries are stored in 3_printouts/part2
uts.get_freq_lemmas_title_cat("Meteorology", 5)
uts.get_freq_lemmas_title_cat("Agriculture", 5)
uts.get_freq_lemmas_title_cat("General Science", 5)

#Generate the plots corresponding to the above example. The plots are stored in 4_plots/part2
uts.plot_freq_lemmas_title_cat("Meteorology", 5)
uts.plot_freq_lemmas_title_cat("Agriculture", 5)
uts.plot_freq_lemmas_title_cat("General Science", 5)
