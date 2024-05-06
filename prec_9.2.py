print('[점수 입력]')
score_list = []
for i in range(3):
    score = int(input(f'#{i+1}? '))
    score_list.append(score)
    
print('[점수 출력]')
print(f'입력 점수: {score_list[0]} {score_list[1]} {score_list[2]}')
avg = sum(score_list) / len(score_list) # sum과 len 함수 사용
print(f'평균: {avg:.1f}') # :.1f를 활용해 소수점 한 자리까지만 출력하도록

print('[검색]')
find_score = int(input('찾고자 하는 점수는? '))
if find_score in score_list: # 예외처리를 위해 list에 있는 값만 탐색하도록
    index = score_list.index(find_score) + 1 # Index Method 호출하여 해당 값을 가진 요소의 index를 찾는다.
    print(f'{find_score}은 {index}번 학생의 점수입니다.')
else:
    print(f'{find_score}은(는) 리스트에 존재하지 않습니다.') 
