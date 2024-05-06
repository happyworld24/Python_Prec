print('[점수 입력]')
score_list = []
for i in range(3):
    score = int(input(f'#{i+1}? '))
    score_list.append(score)
    
print('[점수 출력]')
print(f'입력 점수: {score_list[0]} {score_list[1]} {score_list[2]}')
avg = sum(score_list) / len(score_list) # sum과 len 함수 사용
print(f'평균: {avg:.1f}') # :.1f를 활용해 소수점 한 자리까지만 출력하도록