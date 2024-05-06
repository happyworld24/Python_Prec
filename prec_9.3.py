shopping_bag = [] # 장바구니
print('[구입]')
while True:
    item = input('상품명? ') # 상품 이름을 입력받기 
    if (item == '') : # item이 빈 문자열이면 루프 빠져나가기, enter
        break
    shopping_bag.append(item) # item을 장바구니에 추가
    print(f'장바구니에 {item}가(이) 담겼습니다.')
    
# 장바구니의 모든 상품 이름 출력 (리스트 이름 사용) 
print(f'>>> 장바구니 보기: {shopping_bag}') 