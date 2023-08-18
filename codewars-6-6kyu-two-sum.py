from itertools import product
def two_sum(arr, summ):
#вернет первую найденную пару значений, удовлетворяющих условию    
    for index_x, x in enumerate(arr):
        for index_y, y in enumerate(arr):
            if x + y == summ and index_x != index_y:
                return [index_x, index_y]

    #пройдет двумя циклами весь массив. значительно медленнее
    #return [[index_x, index_y] for index_x, x in enumerate(arr) for index_y, y in enumerate(arr) if x + y == summ and index_x != index_y]
 


print(two_sum([2,2,3], 4))