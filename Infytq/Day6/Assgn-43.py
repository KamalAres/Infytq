#PF-Assgn-43

def find_smallest_number(num):
    #start writing your code here
    f=[]
    flag=True
    temp=num
    while(flag):
        for i in range(1,num+1):
            if num%i==0:
                f.append(i)
        if len(f)==temp:
            flag=False
        else:
            num+=1
            f=[]
    return f.pop()


num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
