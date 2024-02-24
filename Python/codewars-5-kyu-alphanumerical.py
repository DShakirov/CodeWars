import re

def alphanumeric(password):
    return password.isalnum()
    

#password = 'PassW0rd'
password = 'WhPNMZxh9"ia9LXGg4AT05UbGb0zj'
print (alphanumeric(password))