lst = [0, 1, 7, 0, 2, 2, 0, 0, 1, 0]

def pair_zeros(lst):
    counter = 0
    newlst = []
    for digit in lst:
        if digit != 0:
            newlst.append(digit)
        else:
            counter +=1
            if counter %2 != 0:
                newlst.append(digit)
        
        print (digit, newlst)

pair_zeros(lst)