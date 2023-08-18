def beeramid(bonus, price):
    i = 0
    while bonus >= price*(i**2):
        bonus -= price*(i**2)
        print (i, i**2, bonus)
        i += 1
    return i - 1

print(beeramid(21, 1.5))