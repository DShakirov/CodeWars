def count_ips(start, end):
    start, end = start.split('.'), end.split('.')

    return int(end[3])-int(start[3]) + (int(end[2])-int(start[2]))*256 + (int(end[1])-int(start[1]))*65536 + (int(end[0])-int(start[0]))*16777216

print(count_ips("20.0.0.10", "20.0.1.0"))