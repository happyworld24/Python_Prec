def rep_char(c, num):
    print(c * num)

def draw_line_string():
    word = input('글자 입력: ')
    length = len(word)
    rep_char('-',length*2+4)
    print(f'  {word}  ')
    rep_char('-',length*2+4)

draw_line_string()