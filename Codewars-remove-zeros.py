lst = [1,0,2,3,5,0,8,0]
for item in lst:
    if item == 0:
        lst.remove(item)
        lst.append(item)
print(lst)