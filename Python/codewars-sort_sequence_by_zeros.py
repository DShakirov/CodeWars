sequence = [2,2,2,0,5,6,4,0,1,5,3,0,3,2,1,0]


def sort_sequence_by_zeros(sequence):
    
    lst = []
    newlst =[]
    summ = 0
    for digit in sequence:
        if digit !=0:
            newlst.append(digit)
            summ += digit
        else:
            newlst.sort()
            newlst.append(digit)
            newlst.append(summ)
            lst.append((newlst))
            newlst = []
            summ = 0
    lst.sort(key = lambda x: x[-1])
    newlst = []
    for lists in lst:
        lists.pop()
        for digits in lists:
            newlst.append(digits)
    return newlst
print (sort_sequence_by_zeros(sequence))

        
        