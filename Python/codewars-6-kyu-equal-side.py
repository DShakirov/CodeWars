def equal_side_of_array(arr):
    for arr_index in range(len(arr)):
        if sum(arr[:arr_index+1]) == sum(arr[arr_index:]):
            return arr_index
    return -1

print(equal_side_of_array([20,10,-80,10,10,15,35]))