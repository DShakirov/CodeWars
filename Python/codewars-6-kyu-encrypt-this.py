def encrypt_this(text):
    if not text: return ''
    ans = ''
    for word in text.split(' '):
        first_letter_sub = (str(ord(word[0])))
        if len(word) > 2:
            second_letter_sub = word[-1]
            last_letter_sub = word[1]
            ans += first_letter_sub + second_letter_sub + word[2:-1] + last_letter_sub + ' '
        elif len(word) == 2:
            ans += first_letter_sub + word[-1] + ' '
        elif len(word) == 1:
            ans += first_letter_sub + ' '
    return ans.rstrip()


print(encrypt_this("hello world"))