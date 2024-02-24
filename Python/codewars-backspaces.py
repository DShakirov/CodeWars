string ='abc#d##c'

lst =list(string.lstrip('#'))
newlst = []
for item in lst:
    if item != '#':
        newlst.append(item)

    else:
        for item in newlst:
            newlst.pop()
            break
print (newlst)




