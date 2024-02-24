def num_increment(num):
    ciphers = '1234567890'
    string_increment = True
    nums = str(num)
    for i in range(1, len(nums)):
        if ciphers.index(nums[i]) != ciphers.index(nums[i-1]) +1:
            string_increment = False
    if string_increment:
            return True
        
print(num_increment(67890))