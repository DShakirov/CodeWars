def sum_strings(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)[::-1]
    y = y.zfill(max_len)[::-1]
    res = ''
    carry = 0
    for i in range(len(x)):
        if int(x[i]) + int(y[i]) + carry > 9:
            res += str(int(x[i]) + int(y[i]) + carry - 10)
            carry = 1
        else:
            res += str(int(x[i]) + int(y[i]) + carry)
            carry = 0
    if carry:
        res += str(carry)
    return res[::-1]

print(sum_strings('99', '1'))