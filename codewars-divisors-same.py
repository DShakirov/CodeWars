
def get_divisors(cipher):
    divisor = 1 
    for i in range(1, cipher+1):
        if cipher%i ==0:
            divisor +=1
    return divisor

def count_pairs_int(diff, maxint):
    lst = []
    for cipher in range(maxint - diff):
        if get_divisors(cipher+ diff) == get_divisors(cipher):
            lst.append([cipher, cipher+diff])
    return len(lst)
        

print (count_pairs_int(6, 350))