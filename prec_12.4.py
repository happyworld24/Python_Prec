from datetime import datetime
import pickle
import os

class Time:
    def __init__(self, hour=0, min=0):
        self.__hour = hour
        self.__min = min
        
    def display(self):
        return(f'{self.__hour:02}:{self.__min:02}')
        
    def add(self,t_add):
        self.__hour += t_add.__hour
        self.__min += t_add.__min
        if (self.__min >= 60) :
            self.__hour += 1
            self.__min -= 60
        return self   
            
    @staticmethod
    def is_valid(hour, min):
        if (hour >= 0 and hour <=23):
            if (min >= 0 and min <= 59):
                return True
            else :
                return False
        else :
            return False

def get_current_time():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    nowtime = Time(hour,minute)
    return nowtime

def save_time(time):
    with open ('./last.dat', 'wb') as file:
        pickle.dump(time, file)
        
def load_time():
    with open ('./last.dat', 'br') as file:
        nowtime = pickle.load(file)
    return nowtime

if (os.path.exists('./last.dat')) :
    beforetime = load_time()
    print(f'안녕하세요, 마지막으로 {beforetime.display()}에 실행되었습니다.')
    aftertime = get_current_time()
    save_time(aftertime)
    aftertime = load_time()
    print(f'지금은 {aftertime.display()} 입니다.')
    
else:
    print('안녕하세요, 처음 실행되었습니다.')
    nowtime = get_current_time()
    save_time(nowtime)
    nowtime = load_time()
    print(f'지금은 {nowtime.display()} 입니다.')