def get_integer(bit):
    bit = int(bit)
    return bit

def set_all_bits(bit):
    bybit = (1 << bit) - 1
    return bybit

bit = input('설정할 비트 수는? ')
bit = get_integer(bit)
bybit = set_all_bits(bit)
print(bit, '비트를 모두 1로 설정한 수는', bybit, '(', bin(bybit), ') 이다.')
