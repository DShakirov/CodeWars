def defis(word):
    ones = {
    'zero' : 0,
    'one' : 1, 'two' : 2, 'three' : 3,
    'four' : 4, 'five' : 5, 'six' : 6,
    'seven' : 7, 'eight' : 8, 'nine' : 9,
    }
    tens = {
        'ten' : 10, 
    'twenty' : 20, 'thirty' : 30,
    'forty' : 40, 'fifty' : 50, 'sixty' : 60,
    'seventy' : 70, 'eighty' : 80, 'ninety' : 90,
    }
    
    word = word.split('-')
    return tens[word[0]] + ones[word[1]]

def parse_int(string):
    encodings = {
    'zero' : 0,
    'one' : 1, 'two' : 2, 'three' : 3,
    'four' : 4, 'five' : 5, 'six' : 6,
    'seven' : 7, 'eight' : 8, 'nine' : 9,
    'eleven' : 11, 'twelve' : 12,
    'thirteen' : 13,
    'fourteen' : 14, 'fifteen' : 15, 'sixteen' : 16,
    'seventeen' : 17, 'eighteen' : 18, 'nineteen' : 19,
    'ten' : 10, 
    'twenty' : 20, 'thirty' : 30,
    'forty' : 40, 'fifty' : 50, 'sixty' : 60,
    'seventy' : 70, 'eighty' : 80, 'ninety' : 90,
    'hundred' : 100, 'thousand' : 1000, 'million' : 1000000
        }

    string = string.split(' ')
    temp_index = []
    for ind, word in enumerate(string):
        if '-' in word:
            string[ind] = defis(word)
        elif word == 'million':
            string[ind] = string[ind-1] * 1000000
            temp_index.insert(0, ind-1)            
        elif word == 'hundred':
            string[ind] = string[ind-1] * 100
            temp_index.insert(0, ind-1)
        elif word != 'and':
            string[ind] = encodings[word]
        else:
            temp_index.insert(0, ind)
    for i in temp_index:
        string.pop(i)
    if 1000 in string:
        ans = sum(string[:string.index(1000)])*1000 + sum(string[string.index(1000) +1:])
    else:
        ans = sum(string)
    return ans


print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))
print(parse_int("two hundred forty-six"))
print(parse_int("one million"))