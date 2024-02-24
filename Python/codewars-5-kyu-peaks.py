def pick_peaks(arr):
    ans = {"pos":[], "peaks":[]}
    if not arr:
        return ans
    pos = 0
    peak = arr[0]
    for i in range(1, len(arr)):
        print(f'Позиция:{i}, значение:{arr[i]}, previous:{arr[i - 1]}, {arr[i] > arr[i-1]}')
        if arr[i] > arr[i - 1]:
            peak = arr[i]
            pos = i
        elif arr[i] == arr[i-1]:
            continue
        else:
            if not pos in ans["pos"] and pos!= 0:
                ans["pos"].append(pos)
                ans["peaks"].append(peak)
                print(f'Записано. Позиция: {pos} Значение: {peak}')
        #if (arr[i-1] < arr[i] >= arr[i+1]):
            #ans["pos"].append(i)
            #ans ["peaks"].append(arr[i]) 

    return ans
#print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]))
print(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]))
print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]))