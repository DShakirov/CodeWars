def min_umbrellas(weather):
    DRY_WEATHER = ["clear", "sunny", "cloudy", "overcast", "windy"]
    WET_WEATHER = ["rainy", "thunderstorms"]

    counter = 0
    u_at_home = 0
    u_at_work = 0
    for k, j in enumerate(weather):
        if (k == 0) and j in WET_WEATHER:
            counter += 1 
        elif (j in WET_WEATHER) and (weather[k-1] in DRY_WEATHER):
            if (k%2 == 0) and (u_at_work == 0):
                counter += 1
            elif (k%2) == 1 and (u_at_home == 0):
                counter += 1
            elif k%2 == 0 and u_at_work > 0:
                u_at_work -= 1
            elif k%2 == 1 and u_at_home > 0:
                u_at_home -= 1
        elif (j in DRY_WEATHER) and (weather[k-1] in WET_WEATHER):
            if k%2 == 0 and k != 0:
                u_at_work += 1
            elif k%2 == 1:
                u_at_home += 1
        print(k, j, counter, u_at_home, u_at_work)
    return counter

print(min_umbrellas(['clear', 'sunny', 'windy', 'clear', 'windy', 'sunny', 'clear', 'windy', 'windy', 'sunny', 'windy', 'windy', 'sunny', 'windy', 'sunny', 'thunderstorms', 'sunny', 'clear', 'rainy', 'sunny', 'clear', 'clear', 'rainy', 'clear', 'sunny', 'clear', 'sunny', 'clear', 'clear', 'clear', 'windy', 'windy', 'sunny', 'cloudy', 'windy', 'clear', 'windy', 'windy', 'sunny', 'cloudy', 'windy', 'sunny', 'windy', 'windy', 'windy', 'sunny', 'clear', 'windy', 'clear', 'windy', 'thunderstorms', 'windy', 'sunny', 'windy', 'windy', 'rainy', 'sunny', 'rainy', 'sunny', 'windy', 'clear', 'clear', 'clear', 'windy', 'windy', 'clear', 'windy', 'clear', 'sunny', 'sunny', 'clear', 'clear', 'windy', 'clear', 'windy', 'clear', 'sunny', 'clear', 'windy', 'sunny', 'windy', 'windy', 'windy', 'sunny', 'clear', 'clear', 'clear', 'windy', 'clear', 'sunny', 'clear', 'clear', 'clear', 'clear', 'windy', 'sunny', 'windy', 'sunny', 'thunderstorms', 'sunny']))