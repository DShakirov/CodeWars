def multiplication_table(n):
    ans = []
    for i in range (1, n+1):
        cipher = []
        for y in range(1, n+1):
            cipher.append(i*y)
        ans.append(cipher)
    return ans
print (multiplication_table(4)) 