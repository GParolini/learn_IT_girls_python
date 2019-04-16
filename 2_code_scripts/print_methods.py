#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:05:36 2019

@author: giudittaparolini
"""

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
        #new_list.str.strip(" ")
    return new_list

#Get co_authors    
def get_coauthors(mylist, authors_list):
    #all_coauthors = []
    
    #for author in authors_list:
        #author_coauthors = []
        #for item in mylist:
            #if author in item:
                #author_coauthors.append(item)
        #author_coauthors_final = [x for x in author_coauthors if x != []]
        #author_coauthors_final.insert(0,["Coauthors of %s:" % author])
                
        #all_coauthors.append(author_coauthors_final)
        #all_coauthors_final = [x for x in all_coauthors if x != []]
    #return all_coauthors_final

    all_coauthors = []
    
    for author in authors_list:
        author_coauthors = []
        for item in mylist:
            if author in item:
                author_coauthors.append(item)
            else:
                continue
            if author_coauthors != []:
                author_coauthors.insert(0,["Coauthors of %s:" % author])
        #author_coauthors_final = [x for x in author_coauthors if x != []]
        all_coauthors.append(author_coauthors)
        all_coauthors_final = [x for x in all_coauthors if x != []]
    return all_coauthors_final

    
