ineqs = '<><<><><'
ints = (12, 9, 31, 47, 15, 11, 22, 8, 4)
ineqsist = []
for symbols in ineqs:
    if symbols == '<':
        ineqsist.append('less')
    else:
        ineqsist.append('more')
print (ineqsist)
lstints = []
for val in ints:
    print (val)
    lstints.append(val)
lstints.sort()
print(lstints)
ineqsist.sort()
print(ineqsist)