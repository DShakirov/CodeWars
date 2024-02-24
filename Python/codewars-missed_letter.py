def missed_letter(arr):
    expected = chr(ord(arr[0]))
    for letter in arr:
        print(letter, expected)
        if letter == expected:
            expected = chr(ord(letter) +1)
        else:
            return expected
    

print(missed_letter(['a','b','c','e']))