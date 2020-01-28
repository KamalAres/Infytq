#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    l=[]
    if num1<num2:
        for i in range(num1,num2+1):
            temp=i
            rem=0
            sum=0
            while(temp>0):
                rem=temp%10
                sum=sum+rem
                temp=temp//10
            if i%5==0 and i<100 and sum%3==0:
                l.append(i)
                l.sort()
                max_num=l[-1]
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,100)
print(max_num)
