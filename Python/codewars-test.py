def codewars(arr):
    newarr = []
    for x in range(0, len(arr)):
        if arr[x:-x] not in newarr:
            newarr.append(arr[x:-x])
        y = arr[:]
        del y[x:-x]
        if y not in newarr:
            newarr.append(y)
    return newarr

print(codewars([1,2,3,4,5]))