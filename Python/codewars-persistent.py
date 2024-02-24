x = input('Enter a number: ')

def cycle(x):
    lst = list(str(x))
    ans = 1
    for items in lst:
        ans *= int(items)
    return(ans)

counter = 0
while len(str(x)) > 1:
    x = (cycle(x))
    counter += 1
    print(x)

print ('Iteration count = ', counter)
