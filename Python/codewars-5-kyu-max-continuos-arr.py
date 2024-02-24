from itertools import product
def binary_contiguos_array(arr):
    ans = 0
    for i, y in product(range(len(arr)+1), range(len(arr)+1)):
        if arr[i:y].count(0) == arr[i:y].count(1):
            length = len(arr[i:y])
            if length > ans:
                ans = length
    return ans
print(binary_contiguos_array([1,1,0,1,1,0,1,1]))