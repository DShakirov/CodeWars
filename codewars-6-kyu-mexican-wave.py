def mexican_wave(string):
    ans = []
    for i in range(len(string)):
        if string[i].isalpha():
            if i == 0:
                ans.append(string[0].upper()+ string[1:])
            else:
                ans.append(string[:i] + string[i].upper()+ string[i+1:])
    return ans

print(mexican_wave('hello'))