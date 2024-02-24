def strip_comments(string, markers):
    comment = False
    ans = ''
    for letter in string:
        if letter in markers:
            comment = True
            ans = ans.rstrip()
        elif letter == '\n':
            comment = False
        if comment == False:
            ans += letter
    return ans

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))