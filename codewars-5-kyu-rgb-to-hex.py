def rgb_to_hex(r, g, b):
    for item in (r, g, b):
        if item < 0:
            print('00')
        elif item > 255:
            print('FF')    
        else:
            print('{:02X}'.format(item))

rgb_to_hex(-20, 275, 125)