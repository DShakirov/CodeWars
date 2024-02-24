def valid_ISBN10(isbn):
    if len(isbn) != 10:
        return False
    res = 0
    for k, j in enumerate(isbn):
        if k == 9:
            if j == 'X':
                res += 10*(k+1)
            elif j.isnumeric():
                res += int(j)*(k+1)
            else:
                return False
            
        else:
            if j.isnumeric():
                res += int(j)*(k+1)
            else:
                return False
    return res%11 == 0
       
print(valid_ISBN10('1112223339'))
print(valid_ISBN10('1112223339X'))
