#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:05:36 2019

@author: giudittaparolini
"""


#PRINT NANS
import pandas as pd
import os

#read the data
df = pd.read_csv(os.path.join("..","..", "1_data", "bibliography_data.csv"))


df.isna().sum().to_csv(os.path.join("..","..", "3_printouts", "nans.csv"), mode = "a")



#import pandas as pd
import os

#import the full dataset
df = pd.read_csv(os.path.join("..","..", "1_data", "bibliography_data.csv"))

#print in a csv file the columns of the df and their type
df.dtypes.to_csv(os.path.join("..","..", "3_printouts", "columns.csv"), mode="a")

#A FEW USEFUL METHODS WITH COLUMNS

#method for changing the item type from float to integer. Where is the mistake? I cannot understand!
def float_to_int (column):
    for x in column
    print int(x) if type(x) == float






#PRINT FIRST AUTHORS
import pandas as pd
import os

#read the data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#select only the column "Author" in the dataframe and delete the rows with nan values
author_list = df["Author"].dropna()

#delete the duplicate names 
author_list_no_duplicates = list(set(author_list))

#sort in alphabetical orders (according to the first author)
author_list_no_duplicates.sort()

#open a txt file and write the list of titles in alphabetical order
with open(os.path.join("..","..", "3_printouts", "authors_list.txt"), 'w') as outfile:
    for author in author_list_no_duplicates:
        print(author, file=outfile)
        
        
        
#PRINT ALL AUTHORS
import pandas as pd
import os

#read the data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#split the multiple values in the cells of the column "Author" e produces a new dataframe where there are duplicated rows for the splitted values 
reshaped = \
(df.set_index(df.columns.drop("Author",1).tolist())
   .Author.str.split('; ', expand=True)
   .stack()
   .reset_index()
   .rename(columns={0:'Author'})
   .loc[:, df.columns]
)

#select only the column "Author" and drop the nan values
authors = reshaped["Author"].dropna()

#strip the empty spaces at the beginning and at the end of the column entries, otherwise the system cannot sort alphabetically (sort also the white spaces)
authors1 = authors.str.strip(" ")

#use list and set to produce a list of unique author's names
authors_noduplicates = list(set(authors1))

#sort the names in alphabetical order
authors_noduplicates.sort()


#open a txt file and write the list of titles in alphabetical order
with open(os.path.join("..","..", "3_printouts", "authors_all_list.txt"), 'w') as outfile:
    for author in authors_noduplicates:
        print(author, file=outfile)


#PRINT FIRST COAUTHORS
        import pandas as pd
import os

#read the data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#select only the column "Author" in the dataframe and delete the rows with nan values
author_list = df["Author"].dropna()

#delete the duplicate names 
author_list_no_duplicates = list(set(author_list))

#sort in alphabetical orders (according to the first author)
author_list_no_duplicates.sort()

#this UDF goes through every element of a list 
def printCoauthors(my_list):
    new_list = []
    for item in my_list:
        element = item.split(";")
        if element is not None and len(element)>1:
            new_list.append(element)
        else:
            continue
    for element in new_list:
        if element is not None:
            print(element) 
        else:
            continue
    

def search_nested(mylist, val):
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            print i,j
            if mylist[i][j] == val:
                return mylist[i]
    return str(val) + ' not found'


printCoauthors(author_list_no_duplicates)




#print(element, file=open(os.path.join("..","..", "3_printouts", "coauthors.txt"), "a"))


#PRINT LANGUAGE COUNT

import pandas as pd

df = pd.read_csv("cleandata.csv")

lan_counts = df["Language"].value_counts()

lan_counts.to_csv("language_counts.csv", mode = "a", header=["Count"])

#PRINT JOURNAL TITLES
import pandas as pd
import os

#read data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#list itemtypes labels in the data
item_types =list(set(df["Item Type"]))

print(item_types)

journal_articles = df.loc[df['Item Type'] == 'journalArticle']

journal_titles = journal_articles["Publication Title"].dropna()

journal_titles_unique = list(set(journal_titles))

journal_titles_unique.sort()


with open(os.path.join("..","..", "3_printouts", "journal_titles.txt"), 'w') as outfile:
    for title in journal_titles_unique:
        print(title, file=outfile)



#PRINT PUBLICATION TITLES
import pandas as pd
import os

#read the data
df = pd.read_csv(os.path.join("..","..", "1_data", "cleandata.csv"))

#select only the column "Publication Title" in the dataframe and eliminate the rows with nan values
publication_titles = df["Publication Title"].dropna()

#transform the list into a set (that automatically takes care of eliminating duplicates)
publication_title_no_duplicates = set(publication_titles)

#re-transform the set into a list
publication_title_no_duplicates_list = list(set(publication_titles))

#sort the list of publications in alphabetical order
publication_title_no_duplicates_list.sort()

#open a txt file and write the list of titles in alphabetical order
with open(os.path.join("..","..", "3_printouts", "publication_titles.txt"), 'w') as outfile:
    for title in publication_title_no_duplicates_list:
        print(title, file=outfile)