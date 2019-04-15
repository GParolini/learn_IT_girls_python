#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:05:36 2019

@author: giudittaparolini
"""

#Print item type counts
def itemtype_counts(df):
    item_counts = df["Item Type"].value_counts()
    return item_counts


#Print language counts
def lang_counts(df):
    lang_counts = df["Language"].value_counts()
    return lang_counts

#Print publication titles (by item type)
#reports
def print_report_titles(df):
    reports = df.loc[df["Item Type"] == "report"]
    titles = reports["Type"].dropna()
    reports_unique = list(set(titles))
    sorted_reports = sorted(reports_unique)
    return sorted_reports

#thesis
def print_thesis_titles(df):
    thesis = df.loc[df["Item Type"] == "thesis"]
    titles = thesis["Title"].dropna()
    thesis_unique = list(set(titles))
    sorted_thesis = sorted(thesis_unique)
    return sorted_thesis

#journals
def print_journal_titles(df):
    articles = df.loc[df["Item Type"] == "journalArticle"]
    titles = articles["Publication Title"].dropna()
    titles_unique = list(set(titles))
    sorted_titles = sorted(titles_unique)
    return sorted_titles

#magazines
def print_magazine_titles(df):
    articles = df.loc[df["Item Type"] == "magazineArticle"]
    titles = articles["Publication Title"].dropna()
    titles_unique = list(set(titles))
    sorted_titles = sorted(titles_unique)
    return sorted_titles

#newspapers
def print_newspaper_titles(df):
    articles = df.loc[df["Item Type"] == "newspaperArticle"]
    titles = articles["Publication Title"].dropna()
    titles_unique = list(set(titles))
    sorted_titles = sorted(titles_unique)
    return sorted_titles

#books and book sections
def print_book_titles(df):
    books = df.loc[df["Item Type"] == "book"]
    titles1 = list(books["Title"].dropna())
    book_sections = df.loc[df["Item Type"] == "bookSection"]
    titles2 = list(book_sections["Publication Title"].dropna())
    titles1.extend(titles2)
    titles_unique = list(set(titles1))
    sorted_titles = sorted(titles_unique)
    return sorted_titles

#Print first authors
def print_first_authors(df):
    author_list = df["Author"].dropna()
    author_list_no_duplicates = list(set(author_list))
    first_authors = sorted(author_list_no_duplicates)
    return first_authors

#Print the number of publications for each author
def author_counts(df):
    author_counts = df["Author"].value_counts()
    return author_counts        
        
#Print all authors       
def print_all_authors(df):
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


#my_list = print_first_authors(df)
#all_authors_list = print_all_authors(df)
#Print co_authors
def print_multiauthors(my_list):
    new_list = []
    for item in my_list:
        element = item.split(";")
        if element is not None and len(element)>1:
            new_list.append(element)
        else:
            continue
    

def search_coauthors(mylist, val):
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            print (i,j)
            if mylist[i][j] == val:
                return mylist[i]
    return str(val) + ' not found'

def print_coauthors(mylist, all_authors_list):
    coauthors = []
    for item in mylist:
        for author in all_authors_list:
            if all_authors_list.count(author)>0:
                coauthors.append(item)
            else:
                continue
            return coauthors
                