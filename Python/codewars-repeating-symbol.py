from collections import Counter
string = 'ode to joy'

for key, val in Counter(string).items():
    print (key, val)
    if val >1:
        print (key)
        break
