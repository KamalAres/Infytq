#PF-Assgn-33
from collections import OrderedDict
def find_common_characters(msg1,msg2):
    #pass #Remove pass and write your logic here
    '''common=set(msg1)&set(msg2)
    #print(common)
    common=list(common)
    #print(common)
    char=""
    for i in common:
        char=char+i
    return char'''
    char=""
    if msg1==msg2:
        return "".join(OrderedDict.fromkeys(msg1))
    for i in msg1:
        if i in msg2:
            char=char+""+i
    char=char.replace(" ","")
    if char:
        return char
    else:
        return -1

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
