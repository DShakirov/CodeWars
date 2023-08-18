def shortest_word(string):
    return len(min(string.split(' '), key=len))
string = 'Simple, given a string of words, return the length of the shortest word(s).'

print (shortest_word(string))
