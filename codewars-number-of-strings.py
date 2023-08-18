def number_of_letters(string):
    newstr = ''
    slovar = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
        '6':'six', '7':'seven','8':'eight', '9':'nine'}
    def recourse(newstr):
        dlina = ''.join(list(str(len(newstr))))
        if int(dlina) > 9 :
            for nums in list(dlina):
                if nums in slovar.keys():
                    newstr += slovar[nums]
            return newstr
        else:
            newstr = slovar[str(len(newstr))]
        return newstr
    res = []
    string = list(string)
    for nums in string:
        if nums in slovar.keys():
            newstr += slovar[nums]
    res.append(newstr)
    while recourse(newstr) != newstr:
        newstr = recourse(newstr)
        res.append(newstr)
    return res


    

print(number_of_letters('37'))