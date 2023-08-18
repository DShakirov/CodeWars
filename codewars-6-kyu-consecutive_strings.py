def longest_consec(starr, k):
    ans = [''.join(starr[i:i+k]) for i in range(len(starr) -k +1)]
        #ans.append(''.join(starr[i:i+k]))
    ans.sort(key=len, reverse=True)
    return ans[0]
    


print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))