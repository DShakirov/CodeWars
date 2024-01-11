def string_transformer(s):
    reversed_list = list(reversed(s.split(' ')))
    reversed_string = ' '.join(reversed_list)
    return reversed_string.swapcase()

print(string_transformer("Example Input"))