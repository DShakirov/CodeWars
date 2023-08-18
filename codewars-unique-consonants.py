from collections import Counter
def count_consonants(strings):
    consonants = []
    for letter in strings:
        if letter.isalpha() and letter.lower() not in ["a", "e", "i", "o", "u"]:
            consonants += letter.lower()
    print(consonants)
    return len(Counter(consonants))

print (count_consonants('oOZoi4UoqJk'))