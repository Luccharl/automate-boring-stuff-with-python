import re

fhand = open('text_madlibs.txt')
fread = fhand.read()

punctuation = '.?!'


re_texts = re.compile(r'[A-Z]{4,}\.?')
obj_matched = re_texts.findall(fread)

print(obj_matched)
text = fread.split()

for word in range(len(text)):
    for punc in punctuation:
        if punc in text[word] and text[word] in obj_matched:
            replace = input(f'Enter {text[word].lower()}: ')
            text[word] = replace + punc
        elif text[word] in obj_matched:
            replace = input(f'Enter {text[word].lower()}: ')
            text[word] = replace


new_text = ' '.join(text)
print(new_text)
fhand.close()

fhand = open('text_madlibs.txt', 'w')
fwrite = fhand.write(new_text)
fhand.close()











