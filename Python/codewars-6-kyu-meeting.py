def meeting(s):
    s = s.split(';')
    ans = []
    for person in s:
        person = person.split(':')
        ans.append(f'({person[1].upper()}, {person[0].upper()})')
    ans.sort()
    return ''.join(ans)

print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))