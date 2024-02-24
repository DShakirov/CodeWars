import re
def interesting(num, avesome_phrases):
#A number is only interesting if it is greater than 99!
    if num <= 99:
        return False
#Any digit followed by all zeros: 100, 90000
    if re.match(r'[1-9](0)+$',str(num)):
        print(num, 'Продолжительные нули')
        return True
#The digits match one of the values in the awesome_phrases array
    if num in avesome_phrases:
        return True
#Every digit is the same number: 1111
    if len(set(str(num))) == 1:
        print(num, 'Число состоит из одинаковых символов')
        return True
#The digits are sequential, incementing
    ciphers = '1234567890'
    string_increment = True
    nums = str(num).rstrip('0')
    for i in range(1, len(nums)):
        if ciphers.index(nums[i]) != ciphers.index(nums[i-1]) +1:
            string_increment = False
    if string_increment:
            print(num, 'Последовательность возрастающих чисел')
            return True
#The digits are sequential, decrementing‡
    ciphers = '0123456789'
    string_decrement = True
    nums = str(num).rstrip('0')
    for i in range(1, len(nums)):
        if ciphers.index(nums[i]) != ciphers.index(nums[i-1]) -1:
            string_decrement = False
    if string_decrement:
            return True
#The digits are a palindrome
    if str(num)[::-1] == str(num):
        print(num, 'Палиндром')
        return True
    return False
  

def is_interesting(number, awesome_phrases):
    #Возвращаем 2 при точном совпадении
    if interesting(number, awesome_phrases):
        return 2
    #Возвращаем 1 при приближении
    for i in range(number +1, number +3):
        if interesting(i, awesome_phrases):
            return 1
    #Не попали, возвращаем 0
    return 0

print(is_interesting(67890, [1337, 256]))