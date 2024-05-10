# 사용자 정의 함수부
def get_date():
    y = int(input('연도? '))
    m = int(input('월? '))
    d = int(input('일? '))
    return (y, m, d) # 튜플 리턴

# 주 프로그램부
print('당신의 생일을 입력하세요:')
bday = get_date() # 리턴된 튜플을 받는다
print(f'당신의 만 60번째 생일은 {bday[0]+60}년 {bday[1]}월 {bday[2]}일입니다.')