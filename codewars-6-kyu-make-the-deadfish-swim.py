def make_deadfish_swim(commands):
    ans = []
    value = 0
    for instruction in commands:
        if instruction == 'i':
            value +=1
        elif instruction == 'd':
            value -=1
        elif instruction == 's':    
            value = value**2
        elif instruction == 'o':
            ans.append(value)
    return ans

print(make_deadfish_swim("iiisdoso"))