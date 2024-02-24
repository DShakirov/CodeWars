def find_inctantation(string):
    ans = string.split()
    newlist = []
    for word in ans:
        newlist.append(word)
        newlist.append(' ')
    print(newlist)

def morse_code(string):
    newstr = ''
    probels = ''
    ans = ''
    for letter in string:
        if letter in '.-':
            if len(probels)>1: 
                ans += ' '
            newstr += letter
            probels = ''
        elif letter==' ':
            if len(newstr)>0:
                ans += newstr
            newstr = ''
            probels += letter
    print(ans)
    
string = '.... . -.--   .--- ..- -.. .'
morse_code(string)


