def fahrenheit_to_celsius(tem):
    F = tem
    C = 5/9*(F-32)
    print(f'화씨 {F} 도는 섭씨 {C} 도')

def get_real():
    tem = float(input('변환하고자 하는 화씨온도? '))
    return tem

tem = get_real()
fahrenheit_to_celsius(tem)
