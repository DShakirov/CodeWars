from collections import Counter
def scrambles(text1, text2):
    text1 = dict(Counter(text1))
    text2 = dict(Counter(text2))
    for key, val in text2.items():
        if (key not in text1.keys()) or (val > text1[key]):
            return False

    return True
print (scrambles('katas', 'steak'))