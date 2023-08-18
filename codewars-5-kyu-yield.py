def make_looper(string):
    for i in range(len(string)):
        yield print(string[i])

abc = make_looper('abc')
abc()