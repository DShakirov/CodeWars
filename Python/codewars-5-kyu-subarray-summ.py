def subarray(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if sum(arr[i:j+1]) == 0:
                res.append(arr[i:j+1])
    return sorted(res, key = len, reverse=True)[0]
print(subarray([25, -35, 12, 6, 92, -115, 17, 2, 2, 2, -7, 2, -9, 16, 2, -11]))