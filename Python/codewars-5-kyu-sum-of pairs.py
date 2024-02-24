from collections import Counter
def sum_of_pairs(ints,s):
    complement_dict = {}
    
    for i in ints:
        if i in complement_dict:
            return [s-i, i]
        else:
            complement_dict[s - i] = i



print(sum_of_pairs([10, 5, 2, 3, 7, 5], 10))