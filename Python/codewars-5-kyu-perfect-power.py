from math import log

def isPP(n):
    for i in range(2, int(n/2) + 1):
        k = round(log(n, i), 6)
        if k == round(k):
            return([i, int(k)])
    return None

print(isPP(9))