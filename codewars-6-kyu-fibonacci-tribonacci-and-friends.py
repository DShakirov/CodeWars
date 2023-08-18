def xbonacci(signature, n):
    x = len(signature)
    for i in range(len(signature), n):
        signature.append(sum(signature[i-x:i]))
    return signature[:n]
print(xbonacci([0,0,0, 0,1], 10))