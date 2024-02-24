from itertools import product


def get_pins(observed):
    missviews = [
        ['0', '8'],
        ['1', '2', '4'],
        ['1', '2', '3', '5'],
        ['2', '3', '6'],
        ['1', '4', '5', '7'],
        ['2', '4', '5', '6', '8'],
        ['3', '5' '6', '9'],
        ['4', '7', '8'],
        ['0', '5', '7', '8', '9'],
        ['6', '8', '9'],
    ]
    if len(observed) == 1:
        return missviews[int(observed)]
    y = [''.join(missviews[int(i)]) for i in observed]
    pr = []
    for j in product(*y):
        pr.append(''.join(j))
    return pr



print(get_pins('369'))