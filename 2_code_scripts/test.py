#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 00:50:50 2019

@author: giudittaparolini
"""
import pandas as pd



myget_coauthors_nested = [[['Aamodt, O. S.'], ['Aamodt, O. S.', 'Platt, A.W.']],[['Afzal, M.'], ['Throught, T.', 'Afzal, M.']], [['Aikins, G. A.'], ['Aikins, G. A.', 'Fay, A. C.']], [['Aikman, J. M.'], ['Dodge, A. F.', 'Aikman, J. M.']], [['Akamine, E.'], ['Clements, H. F.', 'Akamine, E.', 'Shigeura, G.', 'Moriguchi, S.'], ['Clements, H. F.', 'Shigeura, G.', 'Akamine, E.']], [['Alabouvette, L.'], ['Geslin, H.', 'Alabouvette, L.']], [['Albert, D. W.'], ['Albert, D. W.', 'Hilgeman, R. H.']], [['Albert, T.'], ['Boischot, P.', 'Albert, T.']], [['Alberts, H. W.'], ['Alberts, H. W.', 'et al.']], [['Albertson, F. W.'], ['Albertson, F. W.', 'Weaver, J. E.']], [['Albrecht, B. E.'], ['Albrecht, B. E.', 'Gavrilova, L. G.', 'Lubimenko, V. N.']], [['Albright, W.D.'], ['Albright, W.D.', 'Stokers, J.G.']], [['Aldrich, W. W.'], ['Aldrich, W. W.', 'Work, R. A.'], ['Aldrich, W. W.', 'Work, R. A.', 'Lewis, M. R.'], ['Auchter, E. C.', 'Schrader, A. L.', 'Logasse, F. S.', 'Aldrich, W. W.'], ['Lewis, M. R.', 'Work, R. A.', 'Aldrich, W. W.']], [['Aleksandrov, A.'], ['Aleksandrov, A.', 'Slobodnikov, D.']]]

co_authors_pop = [[['Aamodt, O. S.', 'Platt, A.W.']], [['Throught, T.', 'Afzal, M.']], [['Aikins, G. A.', 'Fay, A. C.']], [['Dodge, A. F.', 'Aikman, J. M.']], [['Clements, H. F.', 'Akamine, E.', 'Shigeura, G.', 'Moriguchi, S.'], ['Clements, H. F.', 'Shigeura, G.', 'Akamine, E.']], [['Geslin, H.', 'Alabouvette, L.']], [['Albert, D. W.', 'Hilgeman, R. H.']], [['Boischot, P.', 'Albert, T.']], [['Alberts, H. W.', 'et al.']], [['Albertson, F. W.', 'Weaver, J. E.']], [['Albrecht, B. E.', 'Gavrilova, L. G.', 'Lubimenko, V. N.']], [['Albright, W.D.', 'Stokers, J.G.']], [['Aldrich, W. W.', 'Work, R. A.'], ['Aldrich, W. W.', 'Work, R. A.', 'Lewis, M. R.'], ['Auchter, E. C.', 'Schrader, A. L.', 'Logasse, F. S.', 'Aldrich, W. W.'], ['Lewis, M. R.', 'Work, R. A.', 'Aldrich, W. W.']], [['Aleksandrov, A.', 'Slobodnikov, D.']]]





def coauthors_flatten(lis):
    new_lis = []
    
    for item in lis:
        for element in item:
            my_element = []
            if type(item) == type([]):
                my_element.extend(flatten(item))
            else:
                my_element.append(item)
        
        new_lis.append(my_element)   
        
    return new_lis

def coauthors_unique(lis):
    new_lis = []
    
    for item in lis:
        new_lis.append(sorted(list(set(item))))
    
    return new_lis




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

def pop_author(myget_coauthors_nested):
    author_list = []
    for item in myget_coauthors_nested:
        for element in item:
            if len(element) == 1:
                author_list.append(element)
                
                flat_list = [item for sublist in author_list for item in sublist]
    
    
    return flat_list




        
authors_list = pop_author(myget_coauthors_nested)



co_authors_flat = coauthors_flatten(co_authors_pop)


co_authors_unique = coauthors_unique(co_authors_flat)



my_dict = {}
combined = dict(zip(authors_list, co_authors_unique))
my_dict = combined


def del_from_dict(my_dict):
    for x in my_dict:
        my_dict[x].remove(x)
    return my_dict
    

diz = del_from_dict(my_dict)
print (diz)

