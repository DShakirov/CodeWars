def data_reverse(data):
    start_position = 0
    ans = []
    new_arr = []
    for i in range(8,len(data) + 1, 8):
        print(start_position, i)
        new_arr.append(data[start_position:i])
        start_position = i
    for x in reversed(new_arr):
        ans += x
    return ans


print(data_reverse([0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]))