import operator
def highest_scoring_word(string):
    newdict = {}
    words  = string.split(' ')
    for word in words: 
        score = 0
        for letter in word:
            score += ord(letter) - 96
        newdict.update({word:score})
    print(words, newdict)
    ans = max(newdict.items(),key=operator.itemgetter(1))[0]
    return ans  


print(highest_scoring_word('aa b'))