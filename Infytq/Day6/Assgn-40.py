#PF-Assgn-40
def is_palindrome(word):
    #pass
    #Remove pass and write your logic here
    reverse=""
    word=word.lower()
    #print(reverse)
    reverse=word[::-1]
    #print(reverse)
    if word==reverse:
        return True
    return False

#Provide different values for word and test your program
result=is_palindrome("Madam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
