from collections import Counter

elect = ["A", "A", "A", "B", "B", "C"]

def get_winner(elect):
    counter = Counter(elect)
    number_to_win = len(elect)/2
    print (counter, number_to_win)
    for key, val in counter.items():
        if val >= number_to_win:
            winner = key
    return winner

print(get_winner(elect))  