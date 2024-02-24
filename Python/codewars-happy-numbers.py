def get_square_of_digits(n):
    newnumber = 0
    lst = list(str(n))
    for digit in lst:
        newnumber += int(digit)**2
    return newnumber

def happy_numbers(n):
    for i in range(10):
        n = get_square_of_digits(n)
        if n == 1:
            return True
    return False

print (happy_numbers(51))