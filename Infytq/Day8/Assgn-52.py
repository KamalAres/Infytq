#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    #pass #Remove pass and write the logic here
    if filter_func==None:
        return sum(list_of_num)
    else:
        return sum(filter_func(list_of_num))

def even(data):
    #pass #Remove pass and write the logic here
    e=[]
    for i in data:
        if i%2==0:
            e.append(i)
    return e

def odd(data):
    #pass #Remove pass and write the logic here
    o=[]
    for i in data:
        if i%2!=0:
            o.append(i)
    return o

sample_data = range(1,11)

sum_of_numbers(sample_data,even)
