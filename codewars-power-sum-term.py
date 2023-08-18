def power_sum_term(n):
    counter = 0
    i = 80
    
    while counter != n:
        i += 1
        
        summ = sum(map(int, list(str(i))))
        #for items in list(str(i)):
            #summ += int(items)
        if summ**len(str(i)) == i:
            counter +=1
    return i

n = 5 
power_sum_term(n)