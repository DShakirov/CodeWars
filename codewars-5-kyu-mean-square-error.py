def solution(array_a, array_b):
    res = 0
    for i in range(len(array_a)):
        res += (array_b[i] - array_a[i])**2
    return res/len(array_a)


print(solution([10, 20, 10, 2], [10, 25, 5, -2]))