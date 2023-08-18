def good_vs_evil(good, evil):
    good = good.split()
    evil = evil.split()
    FORCES_OF_GOOD = {'0': 1, '1': 2, '2': 3, '3': 3, '4': 4, '5': 10}
    FORCES_OF_EVIL = {'0': 1, '1': 2,  '2': 2, '3': 2, '4': 3, '5': 5, '6': 10}
    #power_of_good = 0
    #for unit_power, unit_count in enumerate(good):
        #power_of_good += FORCES_OF_GOOD[str(unit_power)]*int(unit_count)
    power_of_good = sum([FORCES_OF_GOOD[str(unit_power)]*int(unit_count) for unit_power, unit_count in enumerate(good)])
    power_of_evil = sum([FORCES_OF_EVIL[str(unit_power)]*int(unit_count) for unit_power, unit_count in enumerate(evil)])
    if power_of_good > power_of_evil:
        return "Battle Result: Good triumphs over Evil"  
    elif power_of_good > power_of_evil:
        return "Battle Result: No victor on this battle field"
    else:
        return "Battle Result: Evil eradicates all trace of Good"

print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))