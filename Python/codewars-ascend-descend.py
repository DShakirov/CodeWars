maxint = int(input('Enter max: '))
minint = int(input('Enter min: '))
length = int(input('Enter lenght: '))
def ascend_descend_repeat(maxint, minint, length):
    string = ''
    newlst = []
    for item in range (minint, maxint+1):
        newlst.append(str(item))
        string += str(item)
        if len(string) == length:
            break
    print (string, newlst)
    newlst.reverse()
    for item in newlst:
        string += str(item)
        if len(string) == length:
            break
    print (string)
    return string
string = ''
while len(string) < length:
    string += ascend_descend_repeat(maxint, minint, length)
    print (string)