import re

def count_vowels(str):    
    return len(re.findall(r'[aeiou]', str, re.IGNORECASE))

print(count_vowels('foobar')) # 3
print(count_vowels('gym')) # 0
print(count_vowels('aaa')) # 0