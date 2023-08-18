arr1 = [267, 273, 271, 145, 275, 150, 487, 169, 428, 50, 314, 444, 445,
        67, 458, 211, 58, 95, 357, 486, 359, 491, 108, 493, 247, 379]
newdict = {}
prime_counter = 0
max_divisors = 1
for digits in arr1:
    counter = 0
    for i in range(1, digits +1):
        
        if digits % i == 0:
            counter +=1
    

    
    if counter > max_divisors:
        max_divisors = counter
    newdict.update({digits:counter})

ans = [len(arr1)]

newlst = [max_divisors]
lst = []
for key, val in newdict.items():
    if val == max_divisors:
        lst.append(key)
    elif val == 2:
        prime_counter +=1
print (newdict, prime_counter)
ans.append(prime_counter)
lst.sort()
newlst.append(lst)
ans.append(newlst)
print(ans)






