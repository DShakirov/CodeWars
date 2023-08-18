string = str('2000 10003 1234000 44444444 9999 11 11 22 123')
lst = string.split(' ')

newlst = []

for item in lst:
    counter = 0
    
    for digits in list(item):
        counter += int(digits)
        
    newitem = str(item)
    newlst.append((counter, newitem))

print (newlst) 
newlst.sort(key = lambda x: x[1])
newlst.sort(key = lambda x: x[0])

print(newlst)
lst.clear()
for item in newlst:
    lst.append(item[1])
print(lst)
newstr = ' '.join(lst)
print(newstr)