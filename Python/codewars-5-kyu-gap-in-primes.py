def is_prime(x):
    if x%2 == 0:
        return False
    sqrt = int((x)**0.5)
    for i in range(3, sqrt+1):
        if x%i == 0:
            return False
    return True

def gap_in_primes(g, n, m):

    for i in range(n, m):
        if is_prime(i) == True and is_prime(i + g) == True:
            ans = [i, i + g]
            for number in range(i + 1, i+g ):
                print (ans, number, is_prime(number))
                if is_prime(number) == False:
                    continue
                else:
                    ans = None
            if ans: 
                return ans

print(gap_in_primes(2, 100, 110))