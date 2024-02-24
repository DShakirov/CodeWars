word = 'test'

def get_middle(word):
    if len(word) %2 != 0:
        return (word[int(len(word)/2)])
    else:
        return (word[(int(len(word)/2 -1)):(int(len(word)/2)+1)])

print(get_middle(word))
