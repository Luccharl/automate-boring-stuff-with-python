#! python 3
#ch6_mclip.py - multi-clipboard program.

TEXT = {'agree': """I agree, that sounds good to me.""",
        'busy': """Sorry, can we do this later?""",
        'upsell': """Would you like making this weekly donation?"""}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python ch6_mclip.py [keyphrase] - copy paste text')
    sys.exit()
    
keyphrase = sys.arv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Successfully copied to clipboard.')
else:
    print(f'There is no answer for {keyphrase}')