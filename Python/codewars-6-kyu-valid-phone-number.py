import re
def valid_phone_number(phone_number):
    return re.search(r'^[(]\d{3}[)]\s\d{3}[-]\d{4}$',phone_number) != None

print(valid_phone_number("(123) 456-7890"))