#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    if year%400==0:
        leap_year=True
    elif year%100==0:
        leap_year=False
    elif year%4==0:
        leap_year=True
    else:
        leap_year=False
    if month in (1,3,5,7,8,10,12):
        month_length=31
    elif month==2:
        if leap_year:
            month_length=29
        else:
            month_length=28
    else:
        month_length=30
    if day<month_length:
        day=day+1
    else:
        if month==12:
            day=1
            month=1
            year=year+1
        else:
            day=1
            month=month+1
    next_day=day
    next_month=month
    next_year=year

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(31,12,2019)
