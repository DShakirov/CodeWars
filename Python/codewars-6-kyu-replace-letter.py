def replace_letters(word):
    const_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    const_consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    const_vowels = ['a','e','i','o','u']    
    ans = ''
    for letter in word:
        ans_find = False
        letter_index = const_alphabet.index(letter)
        if letter in const_consonants:
            for symbol in const_alphabet[letter_index:]:
                if symbol in const_vowels:
                    ans += symbol
                    ans_find = True
                    break
            if ans_find == False:
                for symbol in const_alphabet:
                    if symbol in const_vowels:
                        ans += symbol
                        break
        if letter in const_vowels:
            print(list(reversed(const_alphabet[:letter_index])))
            for symbol in reversed(const_alphabet[:letter_index]):
                if symbol in const_consonants:
                    ans += symbol
                    ans_find = True
                    break
            if ans_find == False:
                for symbol in reversed(const_alphabet):
                    if symbol in const_consonants:
                        ans += symbol
                        break
        print(letter, symbol)
    return ans              
        
print(replace_letters('codewars'))