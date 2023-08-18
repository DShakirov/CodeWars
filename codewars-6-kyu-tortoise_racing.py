import datetime
#Ready!

def tortoise_racing(speed1, speed2, lead):
    time = lead/(speed2/3600 - speed1/3600)
    print(time)
    time_format = str(datetime.timedelta(seconds=time)).split(':')
    #hours = int(time/3600)
   # minutes = int(((time%3600))/60)
    #secunds = round(((time%3600))%60)
#And the winner is...
    #return [hours, minutes, secunds]
    return list(map(int, time_format))

print(tortoise_racing(477, 502, 103))