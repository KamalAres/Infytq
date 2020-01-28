#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    count=0
    list_of_leap_years=[]
    #leap=False
    while(count<15):
        if given_year%400==0:
            leap=True
        elif given_year%100==0:
            leap=False
        elif given_year%4==0:
            leap=True
        else:
            leap=False
        if leap:
            list_of_leap_years.append(given_year)
            count=count+1
            given_year=given_year+1
            leap=False
        else:
            given_year+=1
    

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
