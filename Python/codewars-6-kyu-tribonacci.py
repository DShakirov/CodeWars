def tribonacci(signature, n):
    for counter in range(n-3):
        print(counter, sum(signature[counter:counter+3]))
        signature.append(sum(signature[counter:counter+3]))
    return signature

print(tribonacci([0, 0, 1], 10))