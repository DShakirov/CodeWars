def is_merge(s, part1, part2):
    
    for i in range(len(s)):
        for k in range(i, len(s)):
            subs = s[i:k]
            if part1 and part2 and part1.startswith(subs) and part2.startswith(subs):
                print(subs)

print(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'))
  