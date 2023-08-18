def sum_of_intervals(intervals):
    intervals = sorted(intervals, key=lambda x:x[0])
    res = intervals[0][1] - intervals[0][0]
    counter = intervals[0]
    print(intervals[0], res, counter)
    for i in range(1,len(intervals)):

        if intervals[i][0] in range(counter[0],counter[1]) and intervals[i][1] in range(counter[0],counter[1]):
            continue
        elif intervals[i][0] in range(counter[0],counter[1]) and intervals[i][1] not in range(counter[0],counter[1]) :
           res += intervals[i][1] - counter[1]
           counter = intervals[i]
        else:
            res += intervals[i][1] - intervals[i][0]
            counter = intervals[i]

        print(intervals[i], res, counter)
    return res

print(sum_of_intervals([(-434, -414), (-93, -74), (43, 255), (17, 349), (275, 487), (133, 245), (-195, 188), (481, 485), (417, 453), (486, 497), (49, 81), (209, 285)]))