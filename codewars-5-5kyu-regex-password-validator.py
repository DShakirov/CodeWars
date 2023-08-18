import re
def regex_password_validator(string):
    #return re.search(r'(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])([0-9a-zA-z]{6,}$)', str)
    return re.search(r'^[0-9a-zA-Z]${6,}', string)

print(regex_password_validator('k2RYGce\\fuT'))