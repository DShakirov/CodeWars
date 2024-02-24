from collections import Counter
def unique_character(string):
    return max(Counter(string).values())<2

print(unique_character('aab'))