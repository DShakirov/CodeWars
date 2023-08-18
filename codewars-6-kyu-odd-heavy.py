#odd - нечетные, even - четные
from itertools import product
def is_odd_heavy(arr):
    odd_arr = []
    even_arr = []
    for element in arr:
        if element%2 == 0:
            even_arr.append(element)
        else:
            odd_arr.append(element)
    print (len(odd_arr), even_arr)
    if len(odd_arr) == 0:
        return False

    return max(even_arr) < min(odd_arr)
    
print(is_odd_heavy([0, 0, 0, 0]))   