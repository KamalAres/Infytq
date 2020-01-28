#PF-Assgn-
def func(l,sum=0,s=0):
    num=[]
    for i in l:
        sum=sum+i
        s=s*10+i
        if sum==10:
            num.append(str(s))
    #print(num)
    return num
def find_ten_substring(num_str):
    #pass
    #Remove pass and write your logic here
    l=[]
    num=[]
    sum=0
    s=0
    for i in num_str:
        l.append(int(i))
    #print(l)

    for i in l:
        if len(l)>0:
            num=num+func(l)
            l=l[1:]
        #num=func(l)
        

    #print(num)  

    
    return num

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
