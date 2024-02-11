# from bs4 import BeautifulSoup
#
# html_text = '<span class="red">Heavens! what a virulent attack!</span>'
# soup = BeautifulSoup(html_text, 'html.parser')
#
# object_tag = soup.find('span')
# print('object_tag: ', object_tag)
# print('attrs: ', object_tag.attrs)
# print('values: ', object_tag.attrs['class'])
# print('text: ', object_tag.text)
import re
# ---------------------------------------------------------------------------

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# soup = BeautifulSoup(html, 'html.parser')
#
# nameList = soup.find_all('span', {'class': 'green'})
# for name in nameList:
#     print(name.string)
#
# princeList = soup.find_all(string='the prince')
# print(princeList)
# print('the prince count: ', len(princeList))

# ---------------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag.children)))
for child in table_tag.children:
    print(child)
    print('-'*30)

desc = soup.find('table',{'id':'giftList'}).descendants
list_desc = list(desc)
print('descendants 개수: ', len(list_desc))

for tag in list_desc:
    print(tag)

for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

for sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
    print(sibling)

sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print('sibling1:', sibling1)
print(ord(sibling1))

sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.next_sibling
print(sibling2)

style_tag = soup.style
print(style_tag.parent)

img1 = soup.find('img', {'src':'../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)


cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4}$)')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))


import re

lookahead1 = re.search('.+(?=won)', '1000 won')
if (lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')
lookahead2 = re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookahead2)

lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)

lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)

lookbehind2 = re.search('(?<=:).+', 'USD: $51')
print(lookbehind2)

lookbehind4 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 applies.')
print((lookbehind4))