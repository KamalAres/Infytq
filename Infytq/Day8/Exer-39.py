#PF-Exer-39
#This verification is based on string match.

principal_amount=4000
duration=12
rate_of_interest=13

simple_interest =lambda principal_amount,duration,rate_of_interest:(principal_amount*duration*rate_of_interest)/100 

if(simple_interest(principal_amount,duration,rate_of_interest)>1000):
    #write your logic here
    print("Platinum Member")
else:
    print("Gold Member")
