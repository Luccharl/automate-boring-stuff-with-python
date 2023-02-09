import sys,webbrowser,pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    
else:
    address = pyperclip.paste()
    
webbrowser.open(f'htps://www.google.com/maps/place/{address}')