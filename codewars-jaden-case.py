def jaden_case(string):
    lst = string.split(' ')
    ans = ''
    for words in lst:
        ans += words.capitalize() + ' '
    return ans.rstrip()

print(jaden_case("How can mirrors be real if our eyes aren't real"))