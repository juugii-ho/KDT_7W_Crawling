from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
# from selenium import webdriver

naver_url = 'https://finance.naver.com/sise/sise_market_sum.naver'

urlrequest = Request(naver_url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode('cp949'), 'html.parser')

names = soup.select('tbody > tr > td > a')
# print(names)
#
name = []
number =[]
url = []
jisooList = []

for n in names[0:22:2]:
    name.append(n.get_text())
    url.append(n.attrs['href'])
    number.append(n.attrs['href'][22:])


def crawling_company(n):
    company_number = number[int(n)]
    company_url = 'https://finance.naver.com/item/main.naver?code=' + company_number
    html = urlopen(company_url)
    soup = BeautifulSoup(html.read().decode('cp949'), 'html.parser')

    jisoo = soup.find('div', {'class': 'rate_info'})
    jisoo1 = jisoo.find_all('span', {'class': 'blind'})

    for j in jisoo1:
        jisooList.append(j.text)

    print(f'''{company_url}
종목명: {name[n]}
종목코드: {number[n]}
현재가: {jisooList[0]}
전일가: {jisooList[3]}
시가: {jisooList[7]}
고가: {jisooList[4]}
저가: {jisooList[8]}''')

    jisooList.clear()


for i in range(10):
    print(f'[{i+1:>2}] {name[i]}')

while True:
    inp = input("주가를 검색할 기업의 번호를 입력하세요(-1:종료): ")
    if inp == '-1':
        print('프로그램 종료')
        break
    else:
        inp = int(inp)-1
        crawling_company(inp)



