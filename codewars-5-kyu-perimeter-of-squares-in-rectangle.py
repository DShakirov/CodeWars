def fibonacci_numbers(n):
    fibonacci_row = [0,1]
    ans = 0
    for i in range(n):
        fibonacci_row.append(fibonacci_row[-1]+fibonacci_row[-2])
    ans = 4*sum(fibonacci_row)

print(fibonacci_numbers(5))
