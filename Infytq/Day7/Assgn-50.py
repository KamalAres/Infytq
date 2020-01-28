#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    word=data.split(" ")
    vowel=["a","e","i","o","u","A","E","I","O","U"]
    #print(word)
    new=[]
    for i in word:
        if len(i)==1 and i in vowel:
            new.append(i)
            continue
        else:
            for j in vowel:
                if j in i:
                    i=i.replace(j,"")
            new.append(i)
    #print(new)
    data=""
    for i in new:
        data=data+i+" "
    return data[:-1]
        

data="I love Python"
print(sms_encoding(data))
