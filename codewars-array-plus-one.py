lst = [4, 3, 2, 5]

def plus_one(lst):
    num = ''
    newlst = []
    for digit in lst:
        num += str(digit)
    num = int(num) +1
    for digit in str(num):
        newlst.append(digit)
    return newlst
plus_one(lst)