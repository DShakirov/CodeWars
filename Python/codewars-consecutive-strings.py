strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 3
counter = 0
newlst = []
lst = []
ans = []
for words in strarr:
    newword = ''
    newlst.append(str(strarr[counter:counter + k]))
    counter = counter +1
    newword = str(''.join(newlst))
    print (newlst)
    newlst.clear()
    lst.clear()
    
    for letters in newword:
        if letters.isalpha():
            if letters != '[]':
                lst.append(letters)
            word = ''.join(lst)
    ans.append(word)
print (ans, max(ans, key =len))
    

