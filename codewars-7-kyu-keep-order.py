def keep_order(arr, val):
    arr.append(val)
    arr.sort()

    print(arr.index(val))


keep_order([1,1,3,4,5],2)