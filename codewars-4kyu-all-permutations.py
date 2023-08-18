import itertools
def permutations(string):
    string = list(string)
    return list({''.join(p) for p in itertools.permutations(string)})

print(permutations(list('aabb')))