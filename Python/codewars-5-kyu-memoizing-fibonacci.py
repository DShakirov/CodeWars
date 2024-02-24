def memo_decorator(func):
    res = [0, 1]
    def wrapper(n):
        nonlocal res
        if n > len(res):
            for i in range(len(res),n + 1):
                if i >= len(res):
                    res.append(func(i))
        return res[n]
    return wrapper

@memo_decorator
def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2)



print(fibonacci(10))
print(fibonacci(15))
print(fibonacci(8))