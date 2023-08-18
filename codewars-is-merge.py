string = 'codewars'
part1 = 'code'
part2 = 'wars'
def is_merge(string, part1, part2):
    oldlst = list(string)
    lstpart1 = list(part1)
    lstpart2 = list(part2)
    lst = lstpart1 + lstpart2
    
    for letter, letters in zip(oldlst, lstpart1, lstpart2):
        print (letter, letters)
        if letter == letters:
            continue
            
                
            
        
        
    print (oldlst, lstpart1, lstpart2)
    return True
    #oldlst.sort()
    #lst.sort()
    #return oldlst == lst

print(is_merge(string, part1, part2))
