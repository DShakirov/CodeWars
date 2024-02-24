def factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans

def is_prime(x):
    if x<0 or (x>2 and x%2 == 0) or x in [0, 1]:
        return False
    sqrt = int((x)**0.5)
    for i in range(3, sqrt+1):
        #print (x,i, x%i)
        if x%i == 0:
            return False
    return True

def sum_for_list(lst):
    divs = []
    for i in lst:
        x = factor(i)
        for fact in x:
            if fact not in divs:
                divs.append(fact)
    divs.sort()
        #if i > max(primes_divisors):
            #if i % 2 == 0:
                #divs.append(i/2)
            #else:
                #divs.append(i)
        #for divisor in primes_divisors:
            #stop_num = abs(max(lst)) if abs(max(lst)) > abs(min(lst)) else abs(min(lst))
            #if divisor > stop_num:
                #break
            #if divisor not in divs and i % divisor == 0:
                #divs.append(divisor)
    res = []
    for divisor in divs:
        summ = 0
        for i in lst:
            if i % divisor == 0:
                summ += i
        res.append([divisor, summ])
    return res

print(sum_for_list([-29804, -4209, -28265, -72769, -31744]))
print(sum_for_list([15, 21, 24, 30, 45]))
print(factor(21))
