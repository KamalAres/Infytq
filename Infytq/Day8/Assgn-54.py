#PF-Assgn-54
def check_anagram(data1,data2):
    #start writing your code here
    list1=[]
    list2=[]
    data1=data1.lower()
    data2=data2.lower()
    #print(data1,data2)
    for i in data1:
        list1.append(i)
    for i in data2:
        list2.append(i)
    #print(list1,list2)
    new1=[]
    new2=[]
    for i in list1:
        new1.append(i)
    for i in list2:
        new2.append(i)
    #print(new1,new2,">>")
    new1.sort()
    new2.sort()
    #print(new1,new2,"ss")
    #print(list1,new1,list2,new2)
    if new1 == new2:
        #print("Yes")
        for i in list1:
            index=list1.index(i)
            #print(index,list1,list2)/////////
            if list2[index]==i:
                #print(list2[index],i)
                return False
                break
    else:
        return False
    return True

print(check_anagram("eat","tea"))
