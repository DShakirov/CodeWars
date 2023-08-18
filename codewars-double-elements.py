from itertools import count
from logging.config import valid_ident


lst = [1,2,3,3,4,5,6,6,8]
counter = {}
for item in lst:
    counter[item] = counter.get(item,0)+1
singles = {element: count for element, count in counter.items() if count == 1}
print (singles)
summ = 0
for key, val in singles.items():
    summ = summ + key
print (summ)