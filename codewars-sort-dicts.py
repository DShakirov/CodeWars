d = {1:2, 2:4, 3:6}
def sort_dict(d):
    lst = []
    for key, val in d.items():
            lst.append((key,val))
    lst.sort(key = lambda x: x[1], reverse = True)
    print(lst)
sort_dict(d)