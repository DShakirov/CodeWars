customer_id = input('Enter customer Id: ')
counter = 0
lstnumbers = []
lstletters = []
for ciphers in reversed(customer_id):
    if counter <=2:
        lstnumbers.append(ciphers)
    else:
        lstletters.append(ciphers)
    counter +=1
lstnumbers.reverse()
lstletters.reverse()
print (lstnumbers,lstletters)
alphabet = 'ABCDEFGHIKLMNOPQRSTVXYZ'
todoletters = int(''.join(lstletters))
numbers = ['a','a','a']
for i in range(todoletters):
    if i in range(26):
        numbers.replace(numbers[2], alphabet[i])
print (numbers, alphabet[i])