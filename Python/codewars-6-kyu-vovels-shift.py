def vovels_shift(string, n):
    vovels_list = ''
    vovels = "aeiou"
    ans = ''
    counter = -1 - n
    for letter in string:
        if letter in vovels:
            vovels_list += letter
    print(vovels_list)
    for letter in string:
        if letter not in vovels:
            ans += letter
        else:
            shift = counter + n
            print(ans, shift)
            if shift >= len(vovels_list):
                shift %= len(vovels_list)
                ans += vovels_list[shift]
            counter += 1
    return ans
print(vovels_shift('This is a test!', 1))