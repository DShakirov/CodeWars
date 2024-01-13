from itertools import combinations
def longest_arr(arr, command):
    result = []
    max_length = 0
    if (command == "<<") or (command == "< <"):#increasing
        for i in range(2, len(arr)+1):
            for combo in combinations(arr, i):
                if list(combo) == sorted(combo) and len(set(combo)) == len(combo):
                    if len(combo) > max_length:
                        result = [list(combo)]
                        max_length = len(combo)
                    elif len(combo) == max_length:
                        result.append(list(combo))
        res = [x for x in result if len(x) > 2]
        return res[0] if len(res) == 1 else res

    if (command == ">>") or (command == "> >"):#decreasing
        for i in range(2, len(arr)+1):
            for combo in combinations(arr, i):
                if list(combo) == sorted(combo, reverse=True) and len(set(combo)) == len(combo):
                    if len(combo) > max_length:
                        result = [list(combo)]
                        max_length = len(combo)
                    elif len(combo) == max_length:
                        result.append(list(combo))
        res = [x for x in result if len(x) > 2]
        return res[0] if len(res) == 1 else res


#print(longest_arr([-1, 3, -34, 18, -55, 60, 118, -64], "<<"))
print(longest_arr([-22, 40, -45, -43, -1, 7, 43, -56], "> >"))