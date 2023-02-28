from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Python'

html = urlopen(url)
bs = BeautifulSoup(html,'html.parser')
bs = BeautifulSoup(html.read(),'html.parser')
print(bs.html.body.h1)
print(bs.h1.text)
# result = html.read()
# print(result)
