def input_scores():
    print('[점수 입력]')
    i = 1
    scores = []
    
    while(True):
        element = int(input(f'#{i}? '))
        if (element < 0) :
            break
        scores.append(element)
        i+=1
    return scores
        
def get_average(list):
    total = 0
    for e in list:
        total += e
    avg = total / len(list)
    return avg

scores = input_scores()
avg = get_average(scores)
print('\n[점수 출력]')
print('개인 점수: ', end = ' ')
for i in range(len(scores)):
    print(scores[i], end=' ')
print(f'\n평균: {avg:.1f}')