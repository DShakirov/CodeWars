def hex_string_to_rgb(hex_string):
    ans = {'r':0, 'g':0, 'b':0}
    res = []
    start_position = 0
    hex_string = hex_string.lstrip('#')
    for i in range(len(hex_string)+1):
        if len(hex_string[start_position:i]) == 2:
            res.append(int(hex_string[start_position:i], 16))
            start_position = i
    for k, j in enumerate(ans.keys()):
        ans[j] = res[k]
    return ans

print(hex_string_to_rgb('#FF9933'))