def fibonacci_sequence():
    fib_seq = [1, 1]
    while True:
        fib_seq.append(fib_seq[-1]+ fib_seq[-2])
        if len(fib_seq) == 30:
            break
    return fib_seq

print(fibonacci_sequence())