def hashtag(str):
    if not str:
        return False
    else:
        ans = '#'
        lst = str.split(' ')
        for word in lst:
            ans += word.capitalize()
        return ans
    

str = " Hello there thanks for trying my Kata"

print (hashtag(str))