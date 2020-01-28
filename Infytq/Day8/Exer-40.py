#PF-Exer-40
#This verification is based on string match.

num1=20
num2=30

div = lambda num1,num2:num1+num2

if(div(num1,num2)%10)==0:
    #write your logic here
    print("Divisible by 10")
else:
    print("Not Divisible by 10")
