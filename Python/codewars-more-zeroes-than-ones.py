
def more_zeroes(string):
 
    lst = []
    for letter in string:
        binary_letter = str(bin(ord(letter))).lstrip('0b')
        if (binary_letter.count('0') > binary_letter.count('1')) and (letter not in lst):
            lst.append(letter)
    return lst
        
  
string = 'abcdeaaa'
print(more_zeroes(string))