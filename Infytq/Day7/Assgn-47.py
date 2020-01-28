#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    l=[]
    l=sentence.split(" ")
    #print(l)
    r=[]
    for i in l:
        i=i[::-1]
        r.append(i)
    #print(r)
    #print(r[0])
    s=""
    temp=""
    for i in range(1,len(r),2):
        #print(r[i])
        if r[i].find('a')>=0:
            r[i]=r[i].replace("a","")
            s=s+"a"
            
            
        if r[i].find('e')>=0:
            r[i]=r[i].replace("e","")
            s=s+"e"
            #print(r[i],temp)
        if r[i].find('i')>=0:
            r[i]=r[i].replace("i","")
            s=s+"i"
        if r[i].find('o')>=0:
            r[i]=r[i].replace("o","")
            s=s+"o"
            #print(r[i],temp)
        if r[i].find('u')>=0:
            r[i]=r[i].replace("u","")
            s=s+"u"
        temp=r[i]
        r[i]=temp[::-1]+s[::-1]
        s=""
    #print(r)
    sentence=""
    for i in r:
        sentence=sentence+i+" "
    return sentence[0:-1]

sentence="She sells sea shells on the sea shore"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
