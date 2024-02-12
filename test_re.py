import re

def test_re(s):
    return re.search(r'\d\.\d{2}', s).group()

print(test_re("Скачать (Exe 7.02 МБ)"))