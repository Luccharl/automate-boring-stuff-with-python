#!python 
#get_comics.py - Download every single comic in a website

import http
import logging
import os,requests,bs4

logging.basicConfig(level=logging.INFO,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #Get the page and request it
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    #Find url of the comic image
    comic = soup.select('#comic img')

    if comic == []:
        print('Could not find comic')
    else:
        comic_url = 'https:' + comic[0].get('src')
        logging.info(comic_url)
        print(f'Downloading image : {comic_url}')
        res = requests.get(comic_url)
        res.raise_for_status()
        
    #Save the image
    # image = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    
    for chunk in res.iter_content(100000):
        logging.info(chunk) # image.write(chunk)
    # image.close()
    
    #previous button'url
    prev_link = soup.select('a[rel=\'prev\']')[0]
    url = 'https://xkcd.com' + prev_link.get('href')
    
print('Download Successful')
    