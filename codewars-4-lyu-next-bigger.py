from itertools import permutations
#def next_bigger(n):
    #ans = []
    #list_n = list(str(n))
    #for perm in permutations(list_n):
        #if int(''.join(perm)) not in ans:
            #ans.append(int(''.join(perm)))
    #ans.sort()
    #pos = sorted(ans).index(n)
    #print(len(ans), pos)
    #if len(ans) > pos +1:
        #return ans[pos+1]
    #else:
        #return -1

def next_bigger(n):
    list_n = list(str(n))
    if len(list_n) <=1:
        return -1
    pivot = 0
    for i in range(len(list_n)):
        if list_n[i] > list_n[i-1]:
            pivot = i -1
    pivot_data = list_n[pivot]
    print(pivot)
    try:
        min_in_right_part = min([x for x in list_n[pivot:] if x>pivot_data])
    except:
        return -1
    min_in_right_part_index = list_n.index(min_in_right_part, pivot)
    print(list_n)
    list_n.pop(min_in_right_part_index)
    print(list_n)
    list_n.insert(pivot, min_in_right_part)
    print(list_n)
    to_sort = sorted(list_n[pivot+1:])
    print(to_sort)
    ans = list_n[:pivot+1] + to_sort
    if int(''.join(ans)) >= n:
        return int(''.join(ans))
    return -1
#82569
#пивот ==3
#минимум ==7
print(next_bigger(69852))