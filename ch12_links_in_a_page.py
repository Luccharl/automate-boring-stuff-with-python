#! python3
#links_in_a_page.py - Opens all links in a webpage
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

import requests,webbrowser,bs4

url = 'https://inventwithpython.com'
res = requests.get(url)
res.raise_for_status()

res_text = bs4.BeautifulSoup(res.text, 'html.parser')

a_elements = res_text.select('a')
logging.debug(a_elements)

for links in range(len(a_elements)):
    url_to_open = a_elements[links].get('href')
    
    if url_to_open != None and url_to_open.startswith('https'):
        #webbrowser.open_new_tab(url_to_open)
        logging.debug(url_to_open)
    else:
        continue