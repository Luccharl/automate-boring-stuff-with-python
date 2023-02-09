#!/usr/bin/env python3
#program_name.py - what it does

import pyperclip

def add_bullet_to_text():

    text = pyperclip.paste()
    lines = text.split('\n')
    
    for sen in range(len(lines)):
        lines[sen] = '* ' + lines[sen]
    
    text = '\n'.join(lines)    
    pyperclip.copy(text)
       
    return 'text added to clipboad'

print(add_bullet_to_text())
    
    