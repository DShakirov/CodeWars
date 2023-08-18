def is_odd(number):
    for z in list(str(number)):
        print(z)
        if int(z) % 2 == 0: 
            return False
     
    return True


def is_prime(number):
    for i in range(2, number): 
        if number%i == 0:
            return False
    return True
print (is_prime(31))