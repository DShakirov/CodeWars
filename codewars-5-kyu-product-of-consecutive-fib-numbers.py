def product_fib(prod):
    fibonacci_row = [0,1]
    for i in range(0, prod +2):
        print(fibonacci_row)
        if fibonacci_row[-1]*fibonacci_row[-2] == prod:
            return [fibonacci_row[-2], fibonacci_row[-1], True]
        elif fibonacci_row[-1]*fibonacci_row[-2] > prod:
            return [fibonacci_row[-2], fibonacci_row[-1], False]
        fibonacci_row.append(fibonacci_row[-1]+fibonacci_row[-2])


print(product_fib(0))