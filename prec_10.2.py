def find_max(list):
    max = list[0]
    for i in range(len(list)):
        if (list[i] > max) :
            max = list[i]
    return max

int_array = []

for i in range(5):
    element = int(input('정수 입력: '))
    int_array.append(element)

max_int = find_max(int_array)

print(f'가장 큰 정수는{max_int}입니다.')