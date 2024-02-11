from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import csv

with open('hollys_branches.csv', 'a', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["지역", "위치(시,구)", "주소", "전화번호"])
    f.close()

pageNumber = 1
for i in range(51):
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={pageNumber}&sido=&gugun=&store='

    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')
    hollysPage = soup.find('tbody')

    loca=[]
    cent=[]
    cent2=[]
    cent3 = []

    location = hollysPage.find_all('td', {'class':'noline center_t'})

    for loc in location:
        loca.append(loc.get_text())
    center = hollysPage.find_all('td', {'class':'center_t'})
    for i in range(1,len(center)+1,6):
        cent.append(center[i].get_text())
        cent2.append(center[i+2].get_text())
        cent3.append(center[i+4].get_text())

    zip1 = list(zip(loca, cent, cent2, cent3))

    zip2 =[]
    for z in zip1 :
        zip2.append(",".join(z))


    with open('hollys_branches.csv', 'a', encoding='utf-8-sig', newline='') as f:
        writer=csv.writer(f)
        for z in zip1:
            writer.writerows([[z[1],z[0], z[2], z[3]] ])
        f.close()

    pageNumber +=1

