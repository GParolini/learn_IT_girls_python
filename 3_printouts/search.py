#Test the search co-authors function (Ramdas, L. A.)
a = pr.search_coauthors(multi_authors, ' Ramdas, L. A.')
print(a)

#Search co-authors
def search_coauthors(mylist, val):
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            if mylist[i][j] == val:
                return mylist[i]
        else:
            return str(val) + ' not found'
