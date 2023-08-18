def sum_of_parts(arr):
    ans_list = []
    ans = 0
    for i in reversed(arr):
        ans +=i
        ans_list.append(ans)
    return reversed(ans_list)


print(sum_of_parts([1, 2, 3, 4, 5, 6]))

#ls = [0, 1, 3, 6, 10], [1, 3, 6, 10], [3, 6, 10], [6, 10], [10], []