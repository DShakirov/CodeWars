def replace_digits_by_words(input):
    digits = {'zero': 0, 'one':1, 'two':2, 'three':3, 'four':4, 'five' : 5, 'six':6, 'seven':7, 'eight':8, 'nine':9 }
    newstring = ''
    for number in input:
        for key, val in digits.items():
            if number == key:
                newstring += val

