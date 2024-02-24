def only_odd_primes(num):
   # def is_odd(number):
       # for z in list(str(number)):
        #``    if int(z) % 2 == 0: 
        #        return False
        #return True
    #def is_prime(number):
        #for i in range(2, number): 
            #if number%i == 0:
                #return False
        #return True
    def is_odd_and_prime(number):
        for z in list(str(number)):
            if int(z) % 2 == 0: 
                return False
        for i in range(2, number):
            if number%i == 0:
                return False
        return True
    prime_list = []
    i = 2
    while True:
        i += 1
        #if is_prime(i) and is_odd(i):
        if is_odd_and_prime(i):
            prime_list.append(i)
            if i> num:
                break
    return [len(prime_list)-1, prime_list[-2], prime_list[-1]]

print (only_odd_primes(20))