def find_cracker(arr):
    scoring = {"A": 30, "B": 20, "C": 10, "D": 5}
    ans = []
    for string in arr:
        grade_sum = 0
        bonus = 20
        #print (string[2], grade_sum, grades, grades.find('C'), grades.find('D'))
        for grade in string[2]:
        
            if grade in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
                bonus = 0
            if grade in scoring.keys():
                grade_sum += scoring[grade]
        if len(string[2])   >  4:
                grade_sum += bonus
        print (string[0], string [1], grade_sum)
        if (grade_sum < string[1]) or (string[1]>200):
            ans.append(string[0])

    return ans
arr = [['name1', 150, ['B', 'A', 'A', 'C', 'A', 'A']], 
       ['name2', 160, ['B', 'A', 'A', 'A', 'A', 'X', 'Y', 'Z']], 
       ['name3', 160, ['B', 'A', 'A', 'A', 'A', 'D']],
       ['name4', 140, ['B', 'A', 'A', 'C', 'A']]]
print (find_cracker(arr))