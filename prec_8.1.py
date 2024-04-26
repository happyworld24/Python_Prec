def input_age():
    age = int(input('나이? '))
    if (age >= 0 and age <= 120):
        return age
    else:
        return False

def is_adult(age):
    if (age >= 19):
        print('당신은 성인입니다.')
    else:
        print('당신은 성인이 아닙니다.')

while (True):
    age = input_age()
    if (age != False):
        is_adult(age)
        break
    