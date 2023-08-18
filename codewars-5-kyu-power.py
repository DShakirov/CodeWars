from itertools import product
def powerset(arr):
    ans = [[],]
    for x,y in product(range(0,len(arr)+1), range(0,len(arr)+1)):
        prime = arr[x:y]
        reverse = arr[y:x]

        print (prime, reverse)
        if not prime in ans:
            ans.append(prime)
        if not reverse in ans:
            ans.append(reverse)
        middle1 = arr[:]
        del middle1[x:y+1]
        if middle1 not in ans:
            ans.append(middle1)
        print (middle1)
        middle2 = arr[:]
        del middle2[y:x+1]
        if middle2 not in ans:
            ans.append(middle2)
    return ans                   
print (powerset([1, 2, 3, 4, 5]), len(powerset([1, 2, 3, 4, 5])))
