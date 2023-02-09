from pathlib import Path
from pprint import pprint
import re

p = Path(Path.cwd())

print("Enter a regular expression (format: r'reg_ex'): ")
user_re = input()

for item in p.glob('*.txt'):
    print(item)
    fhand = open(item)
    fread = fhand.read()
    
    input_regex = re.compile(user_re)
    obj_matched = input_regex.findall(fread)
    
    for item in obj_matched:
        print(item)