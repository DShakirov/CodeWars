from collections import Counter
string = input('Enter a word: ')
def permute_a_palindrome (input): 
    newdict = dict(Counter(input.lower()))
    counter = 0
    for key, val in newdict.items():
        if val %2 == 1:
            counter +=1
    return counter <= 1
print (permute_a_palindrome(string))



