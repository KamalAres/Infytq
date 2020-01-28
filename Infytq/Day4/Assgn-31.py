#PF-Assgn-31
def check_palindrome(word):
    #pass
    #Remove pass and write your logic here
    #temp=word[::-1]
    #print(temp)
    temp=""
    for i in word:
        temp=i+temp
    if temp==word:
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
