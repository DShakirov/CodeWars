def do_readable(seconds):
    return f'{seconds//3600:02}:{seconds%3600//60:02}:{seconds%3600%60:02}'
print (do_readable(3600))