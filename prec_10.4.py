def input_scores():
    print('[점수 입력]')
    i = 1
    lst = []
    
    while(True):
        element = int(input(f'#{i}? '))
        if (element < 0) :
            break
        lst.append(element)
        i+=1
    return lst
        
def get_average(lst):
    total = 0
    for e in lst:
        total += e
    avg = total / len(lst)
    return avg

def search(lst, n):
    if (n in lst):
        return (lst.index(n)+1)
    else :
        return None

scores = input_scores()
avg = get_average(scores)

print('\n[점수 출력]')
print('개인 점수: ', end = ' ')
for i in range(len(scores)):
    print(scores[i], end=' ')
print(f'\n평균: {avg:.1f}')

print('\n[검색]')
n = int(input('찾고자 하는 점수는? '))
res = search(scores, n)
if (res) : 
    print(f'{n}점은 {res}번 학생의 점수입니다.')
else :
    print(f'{n}점을 받은 학생은 없습니다.')