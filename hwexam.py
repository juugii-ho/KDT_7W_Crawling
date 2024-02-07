from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen

html = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8")
soup = BeautifulSoup(html.read(), 'html.parser')

location = soup.find_all('div', {'class': 'title_area _area_panel'})
location1 = soup.find('h2', {'class':'title'})
print(f'현재 위치: ', location1.text)

temp = soup.find_all('div', {'class':'temperature_text'})

print(f'현재 온도:', temp[0].text)

info = soup.find('ul', {'class':'today_chart_list'})
info1 = info.find_all('li')

state = soup.find('span', {'class': 'weather before_slash'})
print(f'날씨 상태: ', state.text)

print('공기 상태:')
for i in info1:
    if i.text!="":
        print(i.text.strip())

print('-'*50)
print('시간대별 날씨 및 온도')
print('-'*50)

time = soup.find('div', {'class':'graph_inner _hourly_weather'})
time1 = time.find_all('li', {'class':'_li _day'})
for t in time1:
    print(t.text)
time2 = time.find_all('li', {'class': '_li'})
for t in time2:
    print(t.text)
# print(time2)