def remov_nb(n):
    result = []
    summ = n*(n+1)//2
    for x in range(1, n + 1):
        y = (summ - x) // (x + 1)
        if y <= n and x * y == (summ - x - y):
            result.append((x, y))
    return result
print(remov_nb(101))