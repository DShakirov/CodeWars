def land_perimeter(arr):
    perimeter = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                if i == 0 or arr[i-1][j] == 'O':
                    perimeter += 1
                if i == len(arr)-1 or arr[i+1][j] == 'O':
                    perimeter += 1
                if j == 0 or arr[i][j-1] == 'O':
                    perimeter += 1
                if j == len(arr[i])-1 or arr[i][j+1] == 'O':
                    perimeter += 1
    return f"Total land perimeter: {perimeter}"
                

arr = ['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO'] 
print(land_perimeter(arr))