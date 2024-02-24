from collections import Counter
def highest_rank(arr):
    return Counter(sorted(arr, reverse=True)).most_common(1)[0][0]
print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))