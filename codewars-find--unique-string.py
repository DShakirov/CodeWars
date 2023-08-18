lst = [ 'silvia', 'vasili', 'victor']

def find_unique(lst):
    newlst = []
    for string in lst:
        word = list(string)
        word.sort()
        newlst.append(''.join(word))
    newlst.sort(key = lambda x: x.casefold())
    print (newlst)
    if newlst[0][0].casefold() != newlst[1][0].casefold():
        ans =  newlst[0]
    else:
        ans  = newlst[-1]
    print (ans)
    for items in lst:
        if sorted(items) == sorted(ans):
            return items

print (find_unique(lst))
