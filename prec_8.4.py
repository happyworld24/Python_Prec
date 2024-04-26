def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year}년은 윤년입니다.')
    else: 
        print(f'{year}년은 평년입니다.')

while(True):
    year = int(input('윤년 여부를 확인할 연도는? '))
    is_leap_year(year)
    ans = input('다른 연도도 확인하겠습니까? ')
    if (ans != 'Y' and ans != 'y'):
        break