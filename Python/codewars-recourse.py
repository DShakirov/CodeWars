def recurse(n):
    slovar = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
            '6':'six', '7':'seven','8':'eight', '9':'nine'}
    res = []
    string = ''
    for nums in str(n):
        string += slovar[nums] 
    res.append(string)    
    while len(string) > 9:
        newstr = ''
        for nums in list(str(len(string))):
            newstr += slovar[nums]
        string = newstr
        res.append(string)
    while string != slovar[str(len(string))]:
        string = slovar[str(len(string))]
        res.append(string)
    return res

print(recurse(37))