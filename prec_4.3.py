def get_integer(time):
    time = int(time)
    return time

def convert_time(time):
    hour = time // 3600
    mid_time = time % 3600
    min = mid_time // 60
    sec = mid_time % 60
    
    print(f'{time} 초는 {hour} 시간 {min} 분 {sec} 초이다.')
    
time = input('변환하고자 하는 시간(초)? ')
time = get_integer(time)
convert_time(time)