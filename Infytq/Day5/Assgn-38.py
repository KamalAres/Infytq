#PF-Assgn-38

def check_double(number):
    #pass
    #Remove pass and write your logic here
    double=number*2
    #print(double)
    double=str(double)
    length=len(double)
    count=0
    for i in str(number):
        if i in double:
            count=count+1
    if count==length:
        if length==len(str(number)):
            #double=int(double)
            return True
    return False

#Provide different values for number and test your program
print(check_double(245))
