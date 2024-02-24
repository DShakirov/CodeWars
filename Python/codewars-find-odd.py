from collections import Counter
x = [1,2,2,3,3,3,4,3,3,3,2,2,1]
ans = dict(Counter(x))
print (ans)
answer = []
for key, val in ans.items():
    if val%2 != 0:
        print(key)
        answer.append(key)
print(answer)
