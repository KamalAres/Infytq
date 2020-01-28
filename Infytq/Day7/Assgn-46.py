#PF-Assgn-46

def nearest_palindrome(number):
    #start writitng your code here
    flag=True
    number=number+1
    while flag:
        temp=number
        reverse=str(temp)
        #print(temp)
        if str(temp)==reverse[::-1]:
            break
        number=number+1
    return temp

number=121
print(nearest_palindrome(number))
