def input_age():
    age = int(input('나이? '))
    if (age >= 0 and age <= 120):
        return age
    else:
        return -1

def is_adult(age):
    if (age >= 19):
        return True
    else:
        return False

age = input_age()
if is_adult(age) == True:
    print('당신은 성인입니다.')
else:
    print('오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!')
