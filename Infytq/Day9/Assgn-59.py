#PF-Assgn-59
def check_perfect_number(number):
    #start writing your code here
    if number==0:
        return False
    factor=[]
    for i in range(1,number+1):
        if number%i==0:
            factor.append(i)
    sum=0
    for i in factor[:-1]:
        sum+=i
    #print(sum)
    if sum==number:
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    #start writing your code here
    new=[]
    for i in no_list:
        if check_perfect_number(i):
            new.append(i)
    return new

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)
