def split_string(string):
    ans = []
    for i in range(len(string)//2):
        ans.append(string[2*i:2*i+2])
    if len(string)%2 == 1:
        ans.append(f'{string[-1]}_')
    return ans
print(split_string('abc'))