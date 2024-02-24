from collections import Counter
def mix(s1,s2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ans = []
    lst1 = Counter(s1)
    lst2 = Counter(s2)
    for letter in alphabet:
        if letter in lst1.keys() and letter not in lst2.keys():
            if lst1[letter]>1:
                ans.append(f'1:{letter*lst1[letter]}/')
        elif letter in lst1.keys() and letter in lst2.keys():
            if lst1[letter]>lst2[letter]>=1:
                ans.append(f'1:{letter*lst1[letter]}/')
            elif lst2[letter]>lst1[letter]>=1:
                ans.append(f'2:{letter*lst2[letter]}/')
            elif lst1[letter]==lst2[letter] and lst1[letter]>1:
                ans.append(f'=:{letter*lst1[letter]}/')
        elif letter in lst2.keys():
            if lst2[letter] >1:
                ans.append(f'2:{letter*lst2[letter]}/')
                

    return ''.join(sorted(ans, key=lambda x:(-len(x), x[0]))).rstrip('/')

print(mix("my&friend&Paul has heavy hats! &", "my friend John has many many friends &"))