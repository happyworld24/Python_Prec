class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        
    def show(self):
        print(f'({self.__x},{self.__y})')
        
    def set(self, x, y):
        if x and y :
            self.__x = x
            self.__y = y
        else :
            return False
    
    def get(self):
        tuple = (self.__x, self.__y)
        return tuple
 
# 사용자 정의 함수부   
def test():
    p1 = Point()
    p2 = Point(2,3)
    
    p1.show()
    p1.set(10,20)
    p1.show()
    
    p2.show()
    
    x,y = p2.get()
    print(f'x={x}, y={y}')
    
# 주 프로그램부
if __name__ == '__main__':
    test()