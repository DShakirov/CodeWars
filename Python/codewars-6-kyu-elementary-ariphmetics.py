def solve(input_string):
    res = []
    input_string = input_string.split('\n')
    for word in input_string:
        x = word.split(' ')
        counter = 0
        next_counter = 0
        print(x)
        for i in range(1, len(x[0])+1):

            if next_counter > 0:
                if int(x[0][-i]) + int(x[1][-i]) + next_counter > 9:
                    next_counter = 1 
                    counter += 1
                else:
                    next_counter = 0
            elif int(x[0][-i]) + int(x[1][-i]) >9:

                next_counter += 1
                counter += 1
            print(int(x[0][-i]), int(x[1][-i]), next_counter)
        res.append(counter)
        ans = ''        
        for result in res:
            if result == 0:
                ans += 'No carry operation\n'
            else:
                ans += f'{result} carry operations\n'
    return ans.rstrip('\n')


print(solve('321 679'))