import re
def detect_pangram(string):
    return len(set(re.sub(r'[^a-zA-Z]', '', string).lower())) == len('abcdefghijklmnopqrstuvwxyz')
print (detect_pangram("The quick, brown fox jumps over the lazy dog!"))