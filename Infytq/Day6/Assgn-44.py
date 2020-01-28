#PF-Assgn-44

def find_duplicates(list_of_numbers):
    #start writing your code here
    dub=[]
    for i in list_of_numbers:
        if list_of_numbers.count(i)>1 and i not in dub:
            dub.append(i)
    #dub=list(set(dub))
    #dub.sort()
    return dub

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
