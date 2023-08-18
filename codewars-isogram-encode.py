def isogram_encode(input, key):
    if key.upper() != 'PATHFINDER' or input.isnumeric() is False:
        return "Incorrect key or input!"
    else:
        
        encode_dict = {1: 'P', 2: 'A', 3: 'T', 4: 'H', 5: 'F', 6: 'I', 7: 'N', 8: 'D', 9: 'E', 0: 'R'}
      
        ans = ''
        for nums in input:

            for key, val in encode_dict.items():
                if int(nums) == key:
                    print (nums)
                    ans += val
        return ans

def isogram_decode(input, key):
    if key.upper() != 'PATHFINDER' or input.isalpha() is False:
        return "Incorrect key or input!"
    else:
        
        encode_dict = {1: 'P', 2: 'A', 3: 'T', 4: 'H', 5: 'F', 6: 'I', 7: 'N', 8: 'D', 9: 'E', 0: 'R'}
      
        ans = ''
        for letters in input:

            for key, val in encode_dict.items():
                if letters == val:
                    
                        ans += str(key)
        return int(ans)

print(isogram_decode('FRR', 'PATHFINDER'))