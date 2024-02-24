import array

def piramid(n):
    if n == 0:
        return []
    ans = []
    arr = []
    for i in range(1, n+1):
        arr.append(1)
        ans.append(arr[:i+1])
    return ans

print(piramid(3))