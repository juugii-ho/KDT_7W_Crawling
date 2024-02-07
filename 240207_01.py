# from urllib.request import urlopen
#
# html = urlopen('https://www.daangn.com/hot_articles')
# print(type(html))
# print(html.read())

# ------------------------------------------------------------------
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
#
# print(bs)
# print(bs.h1)
# print(bs.h1.string)
#
# print(bs.title)
# print('title:', bs.title.string)
#
# ------------------------------------------------------------------
#
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from bs4 import BeautifulSoup
#
# def getTtitle(url, tag):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#
#     try:
#         bsObj = BeautifulSoup(html.read(), 'html.parser')
#         value = bsObj.find(tag)
#     except AttributeError as e:
#         return None
#     return value
#
# tag = 'h1'
# tag = 'h2'
# value = getTtitle('https://www.pythonscraping.com/pages/page1.html', tag)
#
# if value == None:
#     print(f'{tag} could not be found')
# else:
#     print(value)

# ------------------------------------------------------------------

# import requests
# from bs4 import BeautifulSoup
# # url = 'http://www.pythonscraping.com/pages/page1.html'
# # url = 'http://finance.naver.com'
# url = 'http://www.naver.com'
#
#
# html = requests.get(url)
# print('html.encoding:', html.encoding)
# print(html.text)
#
# soup = BeautifulSoup(html.text, 'html.parser')
# print()
# print('h1.string:', soup.h1.string)

# ------------------------------------------------------------------

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# melon_url = 'https://www.melon.com/chart/index.htm'
# html = urlopen(melon_url)
#
# soup = BeautifulSoup(html.read(), 'html.parser')
# print(soup)

# ------------------------------------------------------------------

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# melon_url = 'https://www.melon.com/chart/index.htm'
# html = urlopen(melon_url)
#
# soup = BeautifulSoup(html.read(), 'html.parser')
# print(soup)

# ------------------------------------------------------------------

# from urllib.request import urlopen
# from urllib.request import Request
# from bs4 import BeautifulSoup
# melon_url = 'https://www.melon.com/chart/index.htm'
# # HTTP request 패킷 생성: Request()
# urlrequest = Request(melon_url, headers={'User-Agent': 'Mozilla/5.0'})
# html = urlopen(urlrequest)
# soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
# print(soup)

# ------------------------------------------------------------------

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://www.daangn.com/hot_articles')
# bs = BeautifulSoup(html.read(), 'html.parser')
#
# print(bs.h1)
# print(bs.h1.string.strip())

# ------------------------------------------------------------------

html_example = """
<html lang="en"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>

</body></html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
# #
# print(soup.title)
# print(soup.title.string)
# print(soup.title.get_text())
# print()
#
# print(soup.body)
# print()
#
# print(soup.h1)
# print(soup.h1.string)
# print()
#
# print(soup.a)
# print(soup.a.string)
# print(soup.a['href'])
# print(soup.a.get('href'))
# print()
#
# print(soup.find('div'))
# print()
#
# print(soup.find('div', {'id' : 'text_id2'}))
# print()
#
# div_text = soup.find('div', {"id":"text_id2"})
# print(div_text.text)
# print()
# print(div_text.string)
# print()

# ------------------------------------------------------------------
#
# href_link = soup.find('a', {'class': 'internal_link'})
# href_link = soup.find('a', class_='internal_link')
# #
# # print(href_link)
# # print(href_link['href'])
# # print(href_link.get('href'))
# # print(href_link.text)
#
# print('href_link.attrs: ', href_link.attrs)
# print('class 속성값: ', href_link['class'])
#
# print('values(): ', href_link.attrs.values())
#
# values = list(href_link.attrs.values())
# print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))
#
# href_value = soup.find(attrs={'href':'www.google.com'})
# href_value = soup.find('a', attrs={'href':'www.google.com'})
#
# print('href_value: ', href_value)
# print(href_value['href'])
# print(href_value.string)
#

span_tag = soup.find('span')

print('span tag: ', span_tag)
print('attrs: ', span_tag.attrs)
print('value: ', span_tag.attrs['class'])
print('text', span_tag.string)

div_tags = soup.find_all('div')
print('div+tags length: ', len(div_tags))

for div in div_tags:
    print('--------------------------------')
    print(div)


links = soup.find_all('a')

for alink in links:
    print(alink)
    print(f"url:{alink['href']}, text: {alink.string}")
    print()

link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags)

p_tags = soup.find_all('p', {'id': ['first', 'third']})
for p in p_tags:
    print(p)

    