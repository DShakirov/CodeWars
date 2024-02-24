def delete_nth(order, max_e):
    repeats = {}
    res = []
    for item in order:
        if not item in repeats.keys():
            repeats[item] = 1
        else:
            repeats[item] += 1
        if repeats[item] <= max_e:
            res.append(item)
    return res

print(delete_nth([1,2,3,1,2,1,2,3], 2))