def pig_it(string):
    ans = ''
    lst = string.split(' ')
    for word in lst:
        if word not in ['!', '?']:
            ans += f'{word[1:]}{word[0]}ay '
        else:
            ans += word
    return ans.rstrip()

print (pig_it('Pig latin is cool'))