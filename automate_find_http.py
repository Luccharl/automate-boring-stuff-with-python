import requests,bs4, webbrowser

url = 'https://inventwithpython.com'

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

a_tag = soup.select('a')

for href in a_tag:
    links = href.get('href')
    if links == None:
        continue
    if links.startswith('http'):
        print(links)
        #webbrowser.open(links)
    