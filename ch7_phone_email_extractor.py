import pyperclip, re

text = pyperclip.paste()

def match_phone_email(text):
    
    matches = []
    
    phone_re = re.compile(r'''
                            ((\d{3})|\(\d{3}\))?
                            (\s|-|\.)?
                            (\d{3})
                            (\s|-|\.)
                            (\d{4})
                            ''', re.VERBOSE|re.DOTALL)
    
    email_re = re.compile(r'((\w+)(@)([a-zA-Z]+.[a-zA-Z]{2,4})(.[a-zA-Z]])?)')
    
    for item in phone_re.findall(text):
        phone_num = '-'.join([item[1], item[3], item[5]])
        matches.append(phone_num)
    
    for item in email_re.findall(text):
        matches.append(item[0])
        
    match_text = '\n'.join(matches)
    
    if len(matches) > 0:
        pyperclip.copy(match_text)
        print('Successfully copied to clipboard!')
    else:
        print('No phone numbers of email addresses found')
        
match_phone_email(text)