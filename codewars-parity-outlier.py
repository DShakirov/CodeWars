def parity_outlier(arr):
    oddlst=[]
    evenlst=[]
    for integers in arr:
        if integers%2 == 0:
            evenlst.append(integers)
        else:
            oddlst.append(integers)
    if len(evenlst) == 1:
        return evenlst[0]
    else:
        return oddlst[0]
    
arr = [160, 3, 1719, 19, 11, 13, -21]
print(parity_outlier(arr))