
string = input('Enter a string: ')
xstring = str(string).split()
lst = []
for xwords in xstring:
        if len(xwords) >= 5:
            xreversed = list(xwords)
            xreversed.reverse()
            xwords = ''.join(xreversed)
            lst.append(xwords)
        else:
            lst.append(xwords)
string = ' '.join(lst)
print (string)
