#! python3
#search.py - Opens several search result

import sys, requests, webbrowser, bs4

#request search page and get the cmd agruments
print('searching ...')
res = requests.get('https://pypi.org/search/?q=' + 'boring stuff')
res.raise_for_status() 

#retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Open a browser tab for each result
link_elements = soup.select('.package-snippet')
num_search_result = min(5, len(link_elements))

for link in range(num_search_result):
    url_to_open = 'https://pypi.org' + link_elements[link].get('href')
    print('Openin', url_to_open)
    webbrowser.open_new_tab(url_to_open)