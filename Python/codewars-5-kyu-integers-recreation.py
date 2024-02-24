def list_squared(m, n):
    ans = []
    for i in range(m, n):
        sqt_divisors = i**2
        for x in range(1, i//2 +1):
            if i % x == 0:
                sqt_divisors += x**2
        print (i, sqt_divisors)
        if sqt_divisors**0.5 == int(sqt_divisors**0.5):
            ans.append([i, sqt_divisors])
    return ans

print (list_squared(240, 250))
