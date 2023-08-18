x = input('Enter a number: ')
def cycle(x):
    lst = list(str(x))
    ans = 0
    for items in lst:
        ans += int(items)
    return(ans)

while len(str(x)) > 1:
    x = cycle(x)
print(x)
