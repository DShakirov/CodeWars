def memoize(func):
    res = [0, ]
    def wrapper(n):
        nonlocal res
        if n > len(res)-1:
            for i in range(len(res),n + 1):
                if i >= len(res):
                    res.append(func(i))
        return res[n]
    return wrapper

@memoize
def exp_sum(n):
    if n <= 0:
        return 0
    dp = [1]+[0]*n
    for num in range(1, n+1):
        for i in range(num, n+1):
            dp[i] += dp[i-num]
    return dp[-1]
    
print(exp_sum(1))
print(exp_sum(10)) 
print(exp_sum(50)) 
