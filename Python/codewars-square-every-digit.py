x =input('Enter a number: ')
number = list(x)
squaret = list()
for digit in number:
    digit = int(digit)**2
print(number)
result = int(''.join(map(str, squaret)))
print (result)