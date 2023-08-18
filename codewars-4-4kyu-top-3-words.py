import re
from collections import Counter

def top_3_words(string):
    word_count = Counter(re.findall(r'([a-z][a-z\']*|[a-z\']*[a-z])', string.lower()))
    return [word[0]for word in word_count.most_common(3)]



print(top_3_words("  //wont won't won't")) 