#PF-Tryout
#Start writing your code here
score=79
grade=''
if score<=100 and score>=80:
    grade='A'
elif score<=79 and score>=73:
    grade='B'
elif score<=72 and score>=65:
    grade='C'
elif score<=64 and score>=0:
    grade='D'
else:
    grade='Z'
print(grade)
