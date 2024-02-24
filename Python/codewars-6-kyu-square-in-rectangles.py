def sq_in_rect(lng, width):
    if lng == width:
        return None
    ans = []
    arr = [lng,width]
    while min(arr) > 0:
        ans.append(min(arr))
        arr = [max(arr) - min(arr), min(arr)]
    return ans
    


print(sq_in_rect(20, 14))