def zero_plentyful_array(arr):
    zeros_counter = 0
    group_counter = 0
    for number in arr:
        if number == 0:
            zeros_counter += 1
        else:
            if zeros_counter >= 4:
                group_counter += 1
                zeros_counter = 0
            elif zeros_counter >= 1:
                return 0
    if zeros_counter >= 4:
            group_counter += 1
            zeros_counter = 0
    if zeros_counter == 0:
        return group_counter
    else:
        return 0

arr = [2, 0, 0, 0, 0, 3, 4, 5, 0, 0, 0, 0, 0]
print(zero_plentyful_array(arr))