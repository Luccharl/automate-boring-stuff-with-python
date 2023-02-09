print('Enter english text tobe translated to pig latin: ')
message = input()

VOWELS = ('a','e', 'i', 'o', 'u','y')

pig_latin = [] #words in pig latin
for word in message.split():
    #separate the non-letters at the start of the word
    prefix_non_letter = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letter += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letter)
        continue
        
    #separate the non-letters at the end of the word
    suffix_non_letter = ''
    while not word[-1].isalpha():
        suffix_non_letter += word[-1]
        word = word[:-1]
        
    #check if the word was in uppercase or title case
    was_upper = word.isupper()
    was_title = word.istitle()
    
    #make the word lowercase for translation
    word = word.lower()
    
    #separate the consonants at the start of the word:
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]
        
    #add the pig latin ending to the word
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'
        
    #change the word back to uppercase or title case
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
        
    #add the non letters back to the start or at the end of the word
    pig_latin.append(prefix_non_letter + word + suffix_non_letter)

#join all the wrod back together
print(' '.join(pig_latin))