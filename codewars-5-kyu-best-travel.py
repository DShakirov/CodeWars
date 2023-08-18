from itertools import combinations
def choose_best_sum(t, k, ls):
    ans = [sum(combination) for combination in list(combinations(ls, k)) if sum(combination) <= t]
    return max(ans) if ans else None

print(choose_best_sum(174,3,[50, 55, 57, 58, 60]))