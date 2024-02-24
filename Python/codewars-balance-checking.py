string = "1000.00 \n :125 Market! 125.45 \n 126= Hardware 34.95 \n 127 Video 7.45 \n 128 Book 14.32 \n 129 Gasoline 16.10"
newstring = ''
for letter in string:
    if letter.isnumeric() or letter.isalpha() or letter in [' ', '.',  '\n']:
        newstring += letter
print (newstring)
newlst = []
for item in newstring.split('\n'):

    newlst.append(item.strip().split(' '))
print (newlst)
balance = newlst.pop(0)
balance = float(balance[0])
print(balance)
newstr = 'Original balance is ' + str(balance)
total_expense = 0
for item in newlst:
    total_expense += float(item[2])
    balance -=(float(item[2]))
    item.append('Balance_' + str(round(balance, 2)))
    newstr += '\n' + '_'.join(item)
    print (item ,newstr)


newstr += '\n'+ 'Total_expense__'+str(round(total_expense, 2))
newstr +='\n'+ 'Average_expense__'+str(round(total_expense /len(newlst), 2))
print(newstr)
