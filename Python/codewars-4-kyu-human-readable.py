def human_readable(time):
    if time == 0:
        return 'now'
    ans = []
    years = time//31536000
    if years > 1:
        ans.append(f'{years} years')
    elif years == 1:
        ans.append('1 year')
    days = (time- years*31536000)//86400
    if days > 1:
        ans.append(f'{days} days')
    elif days == 1:
        ans.append('1 day')
    hours =  (time- years*31536000 - days*86400)//3600
    if hours > 1:
        ans.append(f'{hours} hours')
    elif hours == 1:
        ans.append('1 hour')
    minutes = (time- years*31536000 - days*86400 - hours*3600)//60
    if minutes > 1:
        ans.append(f'{minutes} minutes')
    elif minutes == 1:
        ans.append('1 minute')
    seconds = (time- years*31536000 - days*86400 - hours*3600 - minutes*60)
    if seconds > 1:
        ans.append(f'{seconds} seconds')
    elif seconds == 1:
        ans.append('1 second')
    answer = ''
    if len(ans)>1:
        for i in range(len(ans) -1):   
            answer += f'{ans[i]}, '
        answer = answer.rstrip(', ') + f' and {ans[-1]}'
    else: answer = f'{ans[0]}'
    return answer

print (human_readable(3500))