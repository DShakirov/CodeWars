from collections import Counter

def is_isogram(string):
    if type(string) is not str:
        return False
    else:
        counter = Counter(string.casefold())
        anslst = []
        for key, val in counter.items():
        
            print (key, val)
            if key.isalpha():
                anslst.append(val)
        ans = anslst[0]
        for nums in anslst:
            if nums != ans:
                return False
        return True
    
print(is_isogram('Hjelmqvist-Gryb-Zock-Pfund-Wax'))
            
