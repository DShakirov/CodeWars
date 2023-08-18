import re
def valid_ips(strng):
    if re.search(r'\n', strng) :
        return False
    ans = re.search(r'((^[0][.])|(^[1-9]\d?\d?[.])){1}(([0][.])|([1-9]\d?\d?[.])){2}(([0]$)|([1-9]\d?\d?$)){1}',strng)

    if ans == None:
        return False
    for i in ans.group(0).split('.'):
        if int(i) > 255:
            return False
    return True

print(valid_ips('1.2.3.4\n'))
print(valid_ips('184.109.172.243'))

#((^[0][.])|(^[1-2]?[1-9]\d?[.])){1}(([0][.])|([1-2]?[1-9]\d?[.])){2}(([0]$)|([1-2]?[1-9]?\d$)){1}
