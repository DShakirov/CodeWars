string = input('Enter a sequence: ').split()
n = int(input('Enter number of word: '))
m = int(input('Enter multyplier: '))
word = string[n] + '-'
print((word*m).rstrip('-'))

