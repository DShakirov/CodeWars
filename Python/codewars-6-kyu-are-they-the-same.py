def comp(a,b):
    if a == [] == b:
        return True
    elif not a or not b:
        return False
    return sorted(map(lambda x: abs(x), a)) == sorted(map(lambda x: x**0.5, b))

print(comp([2, 2, 3], [4, 9, 9]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))