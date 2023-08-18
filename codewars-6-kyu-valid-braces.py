
def valid_braces(string):
    braces = {'(':')', '{':'}', '[':']'}
    for key, val in braces.items():
        if string.count(key) != string.count(val):
            return False
        for i in range(len(string)):
            if string[i] in braces.keys():
                if (string[i+1]) and (string[i+1] in braces.values()) and (string[i+1] != braces[string[i]]):
                    return False
    return True
print(valid_braces("[(])"))