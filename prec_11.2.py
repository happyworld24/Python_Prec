class Time:
    def __init__(self, hour=0, min=0):
        self.__hour = hour
        self.__min = min
        
    def display(self):
        print(f'{self.__hour:02}:{self.__min:02}')
        
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

# 사용자 정이 함수부
def main():
    t1 = Time(9)
    t2 = Time(9,30)
    
    t1.display()
    t2.display()
    
    later = t1.add(Time(1,15))
    later.display()
    
    if Time.is_valid(25,0):
        print('유효한 시각')
    else:
        print('유효하지 않은 시각')
        
# 주 프로그램부
if __name__ == '__main__':
    main()