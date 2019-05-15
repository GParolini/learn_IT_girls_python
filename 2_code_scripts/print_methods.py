#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:05:36 2019

@author: giudittaparolini
"""
import utilities as ut
import re

#Get item type counts
def itemtype_counts(df):
    item_counts = df["Item Type"].value_counts()
    return item_counts


#Get language counts
def lang_counts(df):
    lang_counts = df["Language"].value_counts()
    return lang_counts

#Get publication titles (by item type)
#reports
def get_report_titles(df):
    reports = df.loc[df["Item Type"] == "report"]
    titles = reports["Type"].dropna()
    reports_unique = list(set(titles))
    sorted_reports = sorted(reports_unique)
    return sorted_reports

#thesis
def get_thesis_titles(df):
    thesis = df.loc[df["Item Type"] == "thesis"]
    titles = thesis["Title"].dropna()
    thesis_unique = list(set(titles))
    sorted_thesis = sorted(thesis_unique)
    return sorted_thesis

#journals
def get_journal_titles(df):
    articles = df.loc[df["Item Type"] == "journalArticle"]
    titles = articles["Publication Title"].dropna()
    titles_unique = list(set(titles))
    sorted_titles = sorted(titles_unique)
    return sorted_titles

#count articles for each journal
def get_art_count_per_journal(df):
    articles = df.loc[df["Item Type"] == "journalArticle"]
    count_per_j = articles["Publication Title"].value_counts()
    return count_per_j

#list authors for each journal
#def get_authors_per_journal(df):
    #articles = df.loc[df["Item Type"] == "journalArticle"]
    #articles_not_anon = articles["Author"].dropna()
    #authors_grouped = articles_not_anon[articles_not_anon["Author"]].groupby("Publication Title")
    #authors = authors_grouped["Author"].unique()
    #return authors

#magazines
def get_magazine_titles(df):
    articles = df.loc[df["Item Type"] == "magazineArticle"]
    titles = articles["Publication Title"].dropna()
    titles_unique = list(set(titles))
    sorted_titles = sorted(titles_unique)
    return sorted_titles

#newspapers
def get_newspaper_titles(df):
    articles = df.loc[df["Item Type"] == "newspaperArticle"]
    titles = articles["Publication Title"].dropna()
    titles_unique = list(set(titles))
    sorted_titles = sorted(titles_unique)
    return sorted_titles

#books and book sections
def get_book_titles(df):
    books = df.loc[df["Item Type"] == "book"]
    titles1 = list(books["Title"].dropna())
    book_sections = df.loc[df["Item Type"] == "bookSection"]
    titles2 = list(book_sections["Publication Title"].dropna())
    titles1.extend(titles2)
    titles_unique = list(set(titles1))
    sorted_titles = sorted(titles_unique)
    return sorted_titles

#Get first authors
def get_first_authors(df):
    author_list = df["Author"].dropna()
    author_list_no_duplicates = list(set(author_list))
    first_authors = sorted(author_list_no_duplicates)
    return first_authors

#Get the number of publications for each author
def author_counts(df):
    author_counts = df["Author"].value_counts()
    return author_counts        
        
#Get all authors       
def get_all_authors(df):
    reshaped = \
    (df.set_index(df.columns.drop("Author",1).tolist())
    .Author.str.split('; ', expand=True)
    .stack()
    .reset_index()
    .rename(columns={0:'Author'})
    .loc[:, df.columns]
    )
    authors = reshaped["Author"].dropna()
    authors1 = authors.str.strip(" ")
    authors_noduplicates = list(set(authors1))
    return sorted(authors_noduplicates)

#Get multi_authors
def get_multiauthors(my_list):
    new_list = []
    for item in my_list:
        element = item.strip("\n").split("; ")
        if element is not None and len(element)>1:
            new_list.append(element)
        else:
            continue
    return new_list

#Get co_authors nested   
def get_coauthors_nested(coauthors, authors):
    all_coauthors = []
  
    for author in authors:
        author_coauthors = []
        for item in coauthors:
            if author in item:
                author_coauthors.append(item)
            else:
                continue
        if author_coauthors != []:
            author_coauthors.insert(0,["%s" % author])
           
        all_coauthors.append(author_coauthors)
        all_coauthors_final = [x for x in all_coauthors if x != []]
        
    return all_coauthors_final
        
def get_coauthors_pop(coauthors_nested):
    for my_list in coauthors_nested:
        my_list.pop(0)
    return coauthors_nested

def get_coauthors_flatten(lis):
    new_lis = []
    
    for item in lis:
        for element in item:
            my_element = []
            if type(item) == type([]):
                my_element.extend(ut.flatten(item))
            else:
                my_element.append(item)
        
        new_lis.append(my_element)   
        
    return new_lis

def get_coauthors_unique(lis):
    new_lis = []
    
    for item in lis:
        new_lis.append(sorted(list(set(item))))
    
    return new_lis

def get_pop_author(mylist):
    author_list = []
    for item in mylist:
        for element in item:
            if len(element) == 1:
                author_list.append(element)
    
        flat_list = [item for sublist in author_list for item in sublist]
    
    return flat_list

def get_dict_coauthors(authors, co_authors):
    my_dict = dict(zip(authors, co_authors))
    return my_dict

def get_dict_clean(my_dict):
    for x in my_dict:
        my_dict[x].remove(x)
    return my_dict


#Get category counts for all the journal articles in the correspondence dataframe
def jourcat_counts(df):
    jourcat_counts = df["Category"].value_counts()
    return jourcat_counts

#Get category counts for all the journal articles and all the years in the correspondence dataframe
def jourcat_year_counts(df):
    jourcat_year_counts = df.groupby(["Category", "Publication Year"]).size()
    return jourcat_year_counts


##########################
#Get the length of all the txt files
def get_length_art(df):
    lengths = []
    for item in df:
        len(item)
        lengths.append(len(item))
    return lengths

#Get the length of one txt file using the file name
def get_length_art_file(my_str):
    return len(my_str)
    


##########################
#Count the words in each paper (by counting white spaces)
def get_whitespaces(df):
    word_count = []
    for item in df:
        item_count = len(re.findall(r' +', item))
        word_count.append(item_count)
    return word_count