#PF-Assgn-30

def encode(message):
    pass
    #Remove pass and write your logic here
    encoded_message=""
    l=[]
    count=1
    for i in range(0,len(message)):
        if i==len(message)-1:
            l.append([message[i],count])
        elif message[i]==message[i+1]:
            count+=1
        else:
            l.append([message[i],count])
            count=1
    for i in l:
        encoded_message=encoded_message+str(i[1])+i[0]
    return encoded_message

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
