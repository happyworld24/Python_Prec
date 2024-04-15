def find_char_type():
    char = ord(input('한 문자 입력? '))
    if (char >=48 and char <= 57):
        return '숫자'
    elif (char >= 65 and char <=90):
        return '알파벳'
    elif (char >= 97 and char <=122):
        return '알파벳'
    elif (char == 32):
        return '공백'

ans = find_char_type()
print(f'{ans} 문자를 입력했습니다.')