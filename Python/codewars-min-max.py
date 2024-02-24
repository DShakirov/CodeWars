from pdb import lasti2lineno


string = '1 9 3 42 -5'
lst = string.split(' ')
print (lst)

newstring = str(min(map(int,lst))) + ' ' + str(max(map(int,lst)))
print (newstring)


