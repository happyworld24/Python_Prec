import os

shopping_bag = [] # 장바구니

# 파일이 존재하면, 파일의 내용을 리스트로 읽어들임
if os.path.exists('./shopping_bag.txt'):
    print('[파일 읽기]\n')
    with open('./shopping_bag.txt', 'r') as file:
        shopping_bag = [line.strip() for line in file] # 각 줄을 리스트의 항목으로 추가
    print(f'>>> 장바구니 보기: {shopping_bag}')

while True:
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        break
    shopping_bag.append(item)
    print(f'장바구니에 {item}가(이) 담겼습니다.\n')

print(f'>>> 장바구니 보기: {shopping_bag}')

# 장바구니의 모든 항목을 파일에 저장
with open('./shopping_bag.txt', 'w') as file:
    for item in shopping_bag:
        file.write(item + '\n') # 각 항목을 줄바꿈 문자와 함께 파일에 쓰기
