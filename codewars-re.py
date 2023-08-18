import re

url = 'http://www.cnet.com'

def domain_name(url):
    match = re.search(r'[./]?(?:www.)?\w+\-?\w+[.]', url)
    s = match[0]
    s = s.replace('www', '')
    s = s.replace('.', '')
    s = s.replace('/', '')
    print(s)
    return s
domain_name(url)