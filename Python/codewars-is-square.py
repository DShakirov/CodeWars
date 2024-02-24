def is_square(n):
    if n < 0 :
        return False
    x = n**0.5
    return x.is_integer()

print (is_square(0))