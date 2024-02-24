string = "4of Fo1r pe6ople g3ood th5e the2"
def sort_by_number(string):
    newlist = []
    lst = string.split(' ')
    for words in lst:
        for symbols in words:
            if symbols.isnumeric():
                words = symbols + words
                
        newlist.append(words)
    newlist.sort()
    lst = []
    for words in newlist:
        words = words.lstrip(words[0])
        lst.append(words)      
    return ' '.join(lst)

print(sort_by_number(string))