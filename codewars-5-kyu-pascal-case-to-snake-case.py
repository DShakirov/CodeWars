def to_underscore(string):
    ans = ''
    for letter in string:
        if letter.isupper():
            ans += f'_{letter.lower()}'
        else:
            ans += letter
    return ans.lstrip('_')

print(to_underscore("TestController"))