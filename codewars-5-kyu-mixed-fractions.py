from math import gcd

def mixed_fraction(s):
    s = list(map(int, s.split('/')))
    int_part = str(int((s[0])/(s[1]))) if int((s[0])/(s[1])) != 0 else '' #целая часть готова к отдаче в ответ
    o = abs(s[0])%abs(s[1])
    if s[0]/s[1] < 0 and not int_part:
        o = (-1) * o
    nod = gcd(o, s[1])
    float_part = f"{int(o/nod)}/{int(abs(s[1])/nod)}" if o != 0 else ''
    if not int_part and not float_part:
        return '0'
    elif int_part and float_part:
        return f"{int_part} {float_part}"
    elif not int_part:
        return float_part
    elif not float_part:
        return int_part

#print(mixed_fraction('42/9'))
#print(mixed_fraction('6/3'))
#print(mixed_fraction('4/6'))
#print(mixed_fraction('0/18891'))
print(mixed_fraction('-10/7'))
print(mixed_fraction('-22/-7'))
print(mixed_fraction('0/18891'))