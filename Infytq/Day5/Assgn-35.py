#PF-Assgn-35

#Global variable
list_of_marks=12, 18, 25, 24, 2, 5, 18, 20, 20, 21
#mark_sum=sum(list_of_marks)
#print(mark_sum)

def find_more_than_average():
    #pass
    #Remove pass and write your logic here
    avg=sum(list_of_marks)/len(list_of_marks)
    #print(avg,len(list_of_marks))
    count=0
    for i in list_of_marks:
        if i>avg:
            count=count+1
    #percentage=0
    #print(count)
    percentage=(count/len(list_of_marks))*100
    #print(percentage)
    return percentage

def sort_marks():
    #pass
    #Remove pass and write your logic here
    #sort_list=[]
    sort_list=list(list_of_marks)
    sort_list.sort()
    return sort_list

def generate_frequency():
    #pass
    #Remove pass and write your logic here
    freq=[0]*26
    count=0
    for i in range(0,26):
        if i in list_of_marks:
            #print(freq)
            #print(i)
            count=list_of_marks.count(i)
            freq[i]=count
            
    return freq

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
