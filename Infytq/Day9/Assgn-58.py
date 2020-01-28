#PF-Assgn-58
def validate_credit_card_number(card_number):
    #start writing your code here
    odd_list=[]
    even_list=[]
    for i in range(0,len(str(card_number)),2):
            odd_list.append(int(str(card_number)[i]))
    odd_list=odd_list[::-1]
    for i in range(1,len(str(card_number)),2):
            even_list.append(int(str(card_number)[i]))
    new=[]
    for i in odd_list:
        if i*2>9:
            temp=i*2
            sum=0
            while(temp>0):
                rem=temp%10
                sum=sum+rem
                temp=temp//10
            new.append(sum)
            continue
        new.append(i*2)
    sum=0
    for i in new:
        sum+=i
    #print(new,sum)
    #print(even_list[::-1])
    for i in even_list:
        sum+=i
    #print(sum)
    if sum%10==0:
        return True
    else:
        return False

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
