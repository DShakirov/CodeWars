lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
p_num ='(' 
counter =0
for item in lst:
    p_num+= str(item)
    counter +=1
    if counter ==3:
        p_num += ') '
    elif counter == 6:
        p_num += '-'
print (p_num)