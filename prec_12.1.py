filename = input('파일명:')
lines = []

with open(f'./{filename}', 'w') as file:
    file.write('안녕하세요, 반갑습니다.\n')
    file.write('이 파일은 테스트 파일 저작을 위해 작성된 텍스트 문서입니다.\n')
    file.write('조금 낯설더라도 포기하지 마세요.\n')

with open (f'./{filename}', 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))

i = 1
for line in lines:
    print(f'{i}: {line}', end='\n')
    i = i+1