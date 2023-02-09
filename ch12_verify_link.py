import pprint
import requests, bs4

res = requests.get('https://google.com')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

a_elements = soup.select('a')

for href in range(len(a_elements)):
    link = a_elements[href].get('href')
    if link.startswith('https://'):       
        #pprint.pprint(link)
        
        page_link = requests.get(link)
        res.raise_for_status()
        
        if page_link.status_code == 404:
            print(f'{link} broken link')
            
    else:
        continue

print('END')
#https://www.labnol.org/internet/101-useful-websites/18078/