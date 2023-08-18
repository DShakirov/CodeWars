str = "hi)((hi)()"
lst = list(str)
for letter in list(str):
    if letter == '(':
        try:
            lst.remove(')')
            lst.remove(letter)
        except:
            continue
print (lst)