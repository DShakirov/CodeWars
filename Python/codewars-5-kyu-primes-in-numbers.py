from collections import Counter
def number_prime(x):
    if x<0 or (x>2 and x%2 == 0) or x in [0, 1]:
        return False
    sqrt = int((x)**0.5)
    for i in range(3, sqrt+1):
        if x%i == 0:
            return False
    return True

def primes_list(num):
    return [i for i in range(1,num) if number_prime(i)]

def primes_factors(n):
    ans_list = []
    ans = ''
    primes_divisors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for divisor in primes_divisors:
        if n%divisor == 0:
            while n%divisor == 0:
                n /= divisor
                ans_list.append(divisor)
    if n != 1: ans_list.append(n)
    for k,j in Counter(ans_list).items():
        if j ==1:
            ans += f'({k})'
        else:
            ans +=f'({k}**{j})'
    return ans

print(primes_factors(933555431))