# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')
#
# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# -------------------------------------------------------------------------
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')
# body_content = bs.find('div', {'id': 'bodyContent'})
#
# pattern = '^(/wiki/)((?!:).)*$'
# for link in body_content.find_all('a', href=re.compile(pattern)):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# -------------------------------------------------------------------------

#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import datetime
# import random
#
# random.seed(datetime.datetime.now())
# # random.seed(None) # Python 3.9 이상
#
# def get_links(articleUrl):
#     html = urlopen('https://en.wikipedia.org' + articleUrl)
#     bs = BeautifulSoup(html, 'html.parser')
#     body_content = bs.find('div', {'id': 'bodyContent'})
#     wikiUrl = body_content.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
#     return wikiUrl
#
# links = get_links('/wiki/Kevin_Bacon')
# print('links 길이: ', len(links))
#
# while len(links) > 0 :
#     newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#     print(newArticle)
#     links = get_links(newArticle)
#
# -------------------------------------------------------------------------
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# pages = set()
# count = 0
#
# def get_links(pageUrl):
#     global pages
#     global count
#     html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     for link in bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 newPage = link.attrs['href']
#                 count += 1
#                 print(f'[{count}]: {newPage}'.format(count, newPage))
#                 pages.add(newPage)
#                 get_links(newPage)
#
# get_links('')

# -------------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
count = 0

def get_links(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find('p').text)
    except AttributeError as e:
        print('this page is missing somthing! Continuing: ', e)
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-'*40)
                count += 1
                print(f'[{count}]: {newPage}')
                pages.add(newPage)
                get_links(newPage)

get_links('')