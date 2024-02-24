def number_prime(x):
    if x<0 or (x>2 and x%2 == 0) or x in [0, 1]:
        return False
    sqrt = int((x)**0.5)
    for i in range(3, sqrt+1):
        #print (x,i, x%i)
        if x%i == 0:
            return False
    return True
print(number_prime(1))