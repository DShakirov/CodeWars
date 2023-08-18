def range_extraction(arr):
    ans = str(arr[0])
    previous = arr[0]
    counter = 0
    for item in arr[1:]:
        if item == previous + 1:
            counter += 1
        else:
            if counter >=3:
                ans += f'-{previous},{item}'
            elif counter ==1:
                ans += f',{previous},{item}'
            else:
                ans += f',{item}'
            counter = 0
        print (item, counter, previous)
        previous = item
    if counter >=2:
        ans += f'-{previous}'
    elif counter == 1:
        ans += f',{previous}'

    return ans.lstrip(',')



print(range_extraction([-82, -79, -77, -75, -74, -73, -70, -68, -67, -66, -64, -62, -60, -58, -55, -52, -49, -48, -45, -43]))