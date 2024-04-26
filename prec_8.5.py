# 입력받은 높이만큼 정수 나열
# 행 담당
def make_l_triangle (h):
    for i in range(1, h+1):
        display_nums(i)
        print()

# 열 담당
def display_nums(n):
    for i in range(1, n+1):
        print(i, end = '')

h = int(input('높이? '))
make_l_triangle(h)

# 입력받은 높이만큼 *나열
# 행 담당
def make_r_triangle (h):
    for i in range(1, h+1):
        display_nums(i)
        print()

# 열 담당
def display_nums(n):
    for i in range(1, h - n + 1):
        print(' ', end = '')
    for j in range(1, n+1):
        print('*', end ='')

h = int(input('높이? '))
make_r_triangle(h)


