num = 70304
length = len(str(num))
counter = 0
newlst = []
for digit in str(num):
    counter +=1
    if digit != '0':
        newlst.append(digit + '0'*(length - counter) + ' ')
ans = '+ '.join(newlst)
print (ans.rstrip()) 