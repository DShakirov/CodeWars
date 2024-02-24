def sort_emotions(arr, order):
    newarr = []
    ourdict = {':D': 4, ':)': 3, ':|': 2, ':(': 1, 'T_T': 0}
    for emotion in arr:
        newarr.append(ourdict[emotion])
    newarr.sort(reverse=order)

    arr = []
    ourdict = dict(map(reversed, ourdict.items()))
    for items in newarr:
        arr.append(ourdict[items])
    return arr
sort_emotions([':D', ':|', ':)', ':(', ':D'], False)
