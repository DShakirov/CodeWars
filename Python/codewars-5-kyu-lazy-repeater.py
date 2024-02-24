def make_looper(string):
    index = 0

    def looper():
        nonlocal index
        char = string[index]
        return char

    return looper
