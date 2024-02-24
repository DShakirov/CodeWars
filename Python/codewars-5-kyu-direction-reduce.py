def direction_reduce(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH",
                 "EAST": "WEST", "WEST": "EAST"}
    direction = []
    previous = ''
    for dir in arr:
        if opposites[dir] == previous:
            direction.pop()
            try:
                previous = direction[-1]
            except:
                previous = ''
        else:
            direction.append(dir)
            previous = dir
        print(dir, previous, direction)
    return direction
            

print (direction_reduce(['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']))
