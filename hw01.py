from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen

html = urlopen("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY")
soup = BeautifulSoup(html.read(), 'html.parser')

data = soup.select('div.tombstone-container')
# print(data[1])

def scraping_use_select(html):
    print('National Weather Service Scraping')
    print('-'*50)
    print('[select 함수 사용]')
    print(f"총 tomestone-container 검색 개수: {len(data)}")
    print('-'*50)

    for d in range(9):
        data1 = data[d].select_one('p.period-name').text
        data2 = data[d].select_one('p.short-desc').text
        data3 = data[d].select_one('p.temp')
        if d > 0 :
            data3 = data3.text
        data4 = data[d].select_one('img')['alt']
        print(f'[Period]: ', data1)
        print(f'[Short desc]: ', data2)
        print(f'[Temperature]: ', data3)
        print(f'[Image desc]: ', data4)
        print('-'*50)


scraping_use_select(html)



def scraping_use_find(html):
    print('National Weather Service Scraping')
    print('-'*50)
    print('[find 함수 사용]')
    print(f"총 tomestone-container 검색 개수: {len(data)}")
    print('-'*50)

    for d in range(9):
        data1 = data[d].find('p', {'class':'period-name'})
        data2 = data[d].find('p', {'class':'short-desc'})
        data3 = data[d].find('p', {'class':'temp'})
        if data3 != None :
            data3 = data3.get_text()
        data4 = data[d].find('img')['alt']
        print(f'[Period]: ', data1.get_text())
        print(f'[Short desc]: ', data2.get_text())
        print(f'[Temperature]: ', data3)
        print(f'[Image desc]: ', data4)
        print('-'*50)


scraping_use_find(html)