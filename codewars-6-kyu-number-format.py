import re
def number_format(n):
    n = str(n)
    ans = ''
    for i in range(1, len(n)+1):
        ans += n[-i]
        print(n[-i])
        if i%3 == 0:
            ans+=','
    print(ans)
    if ans.endswith(',-'):
        return re.sub(r'^(-)(,)','-',ans[::-1])
    elif ans.endswith(','):
        ans = ans[:-1]
    return ans[::-1]

        

print(number_format(100000))