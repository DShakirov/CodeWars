#odd - нечетный, #even - четный
def sort_the_odd(source_array):
    odd_arr = []
    ans = []
    for item in source_array:
        if item % 2 != 0:
            odd_arr.append(item)
    odd_arr.sort(reverse=False)
    odd_counter = 0
    for item in source_array:
        if item % 2 == 0:
            ans.append(item)
        else:
            ans.append(odd_arr[odd_counter])
            odd_counter += 1
    return ans
    

print (sort_the_odd([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))