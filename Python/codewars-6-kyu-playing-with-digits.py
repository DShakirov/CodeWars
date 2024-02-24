def playing_with_digits(n, p):
    sum = 0
    for digit in list(str(n)):
        sum += int(digit) ** p
        p += 1 
    return int(sum/n) if sum%n == 0 else -1

print (playing_with_digits(46288, 3))
