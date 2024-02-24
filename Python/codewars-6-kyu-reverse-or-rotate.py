def rotate_string(strng):
    return strng[1:] + strng[0]

def rev_rot(strng, sz):
#разбиваем строку на подстроки длиной sz
    start_position = 0
    res = []
    result = []
    for i in range(len(strng)+1):
        if len(strng[start_position:i]) == sz:
            res.append(strng[start_position:i])
            start_position = i
    for item in res:
        ans = 0
        for i in item:
            ans += int(i)**3
        if ans%2 == 0:
            result.append(item[::-1])
        else:
            result.append(item[1:] + item[0])
    return ''.join(result)

print(rev_rot("123456987654", 6))
print(rev_rot("66443875", 8))



