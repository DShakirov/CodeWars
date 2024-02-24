x = int(input('Enter a number: '))
ans = 0
for i in range (1,x+1):
    if x%i == 0 :
        print (i)
        ans += 1
print (ans)
