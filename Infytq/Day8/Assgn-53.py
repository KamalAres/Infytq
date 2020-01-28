#PF-Assgn-53
#This verification is based on string match.
import re
poem='''
It takes strength for being certain,
It takes courage to have doubt.
It takes strength for challenging alone,
It takes courage to lean on another.
It takes strength for loving other souls,
It takes courage to be loved.
It takes strength for hiding our own pain,
It takes courage to help if it is paining for someone.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

#Write your logic here for question 1
print(poem.count('v'))
l=[]
l=poem.split("\n")
#print(l)
new=""
for i in l:
    new=new+i+" "
print(new[1:-1])
if re.search(r"co",poem):
    poem=poem.replace("co","Co")
if re.search(r"ch",poem):
    poem=poem.replace("ch","Ch")
print(poem)
if re.search(r"ai",poem):
    poem=re.sub(r"ai(\w{3})",r"ai*\*",poem)
if re.search(r"hi",poem):
    poem=re.sub(r"hi(\w{3})",r"hi*\*",poem)
print(poem)
'''
print(#Write your regular expression here for question 2)

print()
print(#Write your regular expression here for question 3)

print()
print(#Write your regular expression here for question 4)
'''
