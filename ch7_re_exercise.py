#21
import re,pyperclip

name = re.compile(r'^[A-Z][a-zA-Z]+\sWatanabe')
obj = name.search('RoboCop Watanabe')
#print(obj.group())

#22

text = pyperclip.paste()
sentence = re.compile(r'((Alice|Bob|Carol)\s(pets|eats|throws)\s(apples|cats|baseballs)\.)', re.I)
obj = sentence.findall(text)
#print(obj)

#20

number = re.compile(r'^\d{1,3}(,\d{3})*$')
num_obj = number.search('1234')
print(num_obj.group())