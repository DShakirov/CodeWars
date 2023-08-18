def int32_to_ip(int32):
    int32 = str(bin(int32)).lstrip('0b')
    length = 32 - len(int32)
    int32 = '0'*length + int32
    start = 0
    res = ''
    for i in range(1, 33):
        if i%8 == 0:
            res += str((int((int32[start:i]),2))) + '.'
            start = i
    return res.rstrip('.')
print(int32_to_ip(2149583361))
print(int32_to_ip(32))

x = int('32',2)
print(x)