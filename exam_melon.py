
import requests
from bs4 import BeautifulSoup

def 멜론():
    if __name__ == "__main__":
        RANK = 100
    
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        req = requests.get('https://www.melon.com/chart/day/index.htm', headers = header)
        html = req.text
        parse = BeautifulSoup(html, 'html.parser')
    
        titles = parse.find_all("div", {"class": "ellipsis rank01"}) 
        singers = parse.find_all("div", {"class": "ellipsis rank02"}) 
        albums = parse.find_all("div",{"class": "ellipsis rank03"})
    
        title = []
        singer = []
        album = []
        tnumber= []
        snumber= []

        titles2 = parse.select('div.ellipsis rank01')
        print(titles2)
        # for title in titles2:
        #     print(title['ellipsis rank01'])

        # for t in titles:
        #     title.append(t.find('a').text)
    
        # for s in singers:
        #     singer.append(s.find('span', {"class": "checkEllipsis"}).text)

        # for n in titles:
        #     tnumber.append(n.find('a'))

        # for s in singers:
        #     snumber.append(s.find('span', {"class": "checkEllipsis"}))

        # a = list(zip(title, singer))
        # for b in a:
        #     print(", ".join(b))

멜론()