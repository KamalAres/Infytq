#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    new_salary=0
    percentage=0
    if job_level==3:
        percentage=current_salary*0.15
    elif job_level==4:
        percentage=current_salary*0.07
    elif job_level==5:
        percentage=current_salary*0.05
    else:
        percentage=current_salary*0
    new_salary=current_salary+percentage

    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,3)
print(new_salary)
