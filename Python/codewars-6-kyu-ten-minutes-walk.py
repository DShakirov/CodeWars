
def ten_minutes_walk(walk):
    if len(walk) != 10:
        return False
    #opposites = {'n':'s', 's':'n', 'w':'e', 'e':'w'}
    #res = []
    #for step in walk:
        #print (res, step)
        #if opposites[step] in res:
            #res.remove(opposites[step])
        #else:
            #res.append(step)
    #return res == []



print(ten_minutes_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))