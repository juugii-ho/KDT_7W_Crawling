
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

head = soup.select_one('head')
print(head)
print('head.txt: ', head.text.strip())

h1 = soup.select_one('h1')
print(h1)


footer = soup.select_one('h1#footer')
print(footer)

class_link=soup.select_one('a.internal_link')
print(class_link)

print(class_link.string)
print(class_link['href'])
print()

link1 = soup.select_one('div#link> a.external_link')
print(link1)
print()

link_find = soup.find('div', {'id': 'link'})
external_link = link_find.find('a', {'class':'external_link'})
print('find external_link: ', external_link)
print()

link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)

h1_all = soup.select('h1')
print('h1_all ', h1_all)
print()

url_links = soup.select('a')
for link in url_links:
    print(link['href'])
print()

div_urls = soup.select('div#class1>a')
print(div_urls)
print(div_urls[0]['href'])
print()

div_urls2 = soup.select('div#class1 a')
print(div_urls2)
print()

h1 = soup.select('#heading, #footer')
print(h1)
print()

url_links = soup.select('a.external_link, a.internal_link')
print(url_links)

national_anthem = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>애국가</title>
</head>
<body>
    <div>
        <p id="title">애국가</p>
        <p class="content">
            동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>                
    </div>
</body>
</html>
'''

soup = BeautifulSoup(national_anthem, 'html.parser')
print(soup.select_one('p#title').string)

contents = soup.select('p.content')
for content in contents:
    print(content.text)