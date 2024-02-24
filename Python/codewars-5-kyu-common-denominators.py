def convert_fracts(lst):
    for i in range(1, 100):
        denom = 0
        counter = 0
        for fract in lst:
            if i % fract[1] == 0:
                print(i, fract[1])
                counter += 1
                if counter == len(lst):
                    denom = i
        if denom:
            break
    if not denom: 
        denom = 1
        for fract in lst:
            denom *= fract[1]  
    print(denom)  
    res = []
    for fract in lst:
        res.append([fract[0]*int(denom/fract[1]), denom])
    return res
print(convert_fracts([[1, 1], [3, 1], [4, 1], [5, 1]]))