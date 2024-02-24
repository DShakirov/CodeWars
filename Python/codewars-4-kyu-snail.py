def snail(snail_map):
    res = []
    direction = 'east'
    k = 0
    j = 0
    length = sum([(len(x)) for x in snail_map])
    while len(res) < length:

        if direction == 'east':
            if j < len(snail_map[k]) - 1:
                    if snail_map[k][j] in res:
                        j +=1
                    elif snail_map[k][j+1] in res:
                        res.append(snail_map[k][j])
                        direction = 'south'
                    else:
                        res.append(snail_map[k][j])
                        j += 1
            else:
                direction = 'south'

        elif direction == 'south':
            if k < len(snail_map) - 1:
                if snail_map[k][j] in res:
                    k +=1
                elif snail_map[k+1][j] in res:
                    res.append(snail_map[k][j])
                    direction = 'west'
                else:
                    res.append(snail_map[k][j])
                    k +=1
            else:
                direction = 'west'
        
        elif direction == 'west':
            if j > 0:
                if snail_map[k][j] in res:
                    j -= 1
                elif snail_map[k][j-1] in res:
                    res.append(snail_map[k][j])
                    direction = 'north'
                else:
                    res.append(snail_map[k][j])
                    j -= 1
            else:
                direction = 'north'

        elif direction == 'north':
            if k > 0:
                if snail_map[k][j] in res:
                    k -=1
                if snail_map[k-1][j] in res:
                    res.append(snail_map[k][j])
                    direction = 'east'
                else:
                    res.append(snail_map[k][j])
                    k -= 1
            else:
                direction = 'east'
        print(k, j, res, direction)
    return res       


print(snail([[1,2,3], [4,5,6], [7,8,9]]))
