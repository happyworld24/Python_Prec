def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else: 
        return False

def month_days(month):
    if(month == 2):
        if (is_leap_year(year)):
            return 29
        else:
            return 28
    elif(month % 2 == 0):
        return 30
    else:
        return 31
    
year = int(input('연도? '))
month = int(input('월? '))
day = month_days(month)

print(f'{year}년 {month}월은 {day}일까지 있습니다.')