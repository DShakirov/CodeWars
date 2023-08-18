from collections import Counter

seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]

def find_odd_int(seq):
    for key, val in Counter(seq).items():
        print (key, val)
        if val %2 == 1 :
            return key

print(find_odd_int(seq))