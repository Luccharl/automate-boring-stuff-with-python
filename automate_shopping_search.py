from os import link
import requests, bs4, webbrowser,pprint

url = 'https://www.lazada.com.ph/catalog/?spm=a2o4l.home.search.1.1f65359dYWP1vk&q=speaker&_keyori=ss&from=search_history&sugg=speaker_0_1'

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

a_tag = soup.select('a')

for links in a_tag:
    href = links.get('href')
    if href is None:
        continue
    if href.startswith('//www.lazada.com.ph/'):
        print(href)