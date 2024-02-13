# import csv
#
# csvFile = open('test.csv', 'w', encoding='UTF-8')
#
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(('number', 'number+2', '(number+2)^2'))
#
#     for i in range(10):
#         writer.writerow(((i, i+2, pow(i+2,2))))
# except Exception as e:
#     print(e)
# finally:
#     csvFile.close()

# --------------------------------------------------------------------
#
# import csv
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
# bs = BeautifulSoup(html, 'html.parser')
#
# table = bs.find_all('table', {'class': 'wikitable'})[0]
# rows = table.find_all('tr')
#
# csvFile = open('editors.csv', 'wt', encoding='utf-8')
# writer = csv.writer(csvFile)
#
# try:
#     for row in rows:
#         csvRow = []
#         for cell in row.find_all(['th','td']):
#             print(cell.text.strip())
#             csvRow.append(cell.text.strip())
#         writer.writerow(csvRow)
# finally:
#     csvFile.close()

# --------------------------------------------------------------------

#
# import csv
# from urllib.request import urlopen
# import pandas as pd
# from bs4 import BeautifulSoup
# from html_table_parser import parser_functions as parse
#
# html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
# bs = BeautifulSoup(html, 'html.parser')
#
# table = bs.find('table', {'class': 'wikitable'})
# table_data = parse.make2d(table)
#
# print('[0]:', table_data[0])
# print('[1]:', table_data[1])
#
# df = pd.DataFrame(table_data[2:], columns=table_data[1])
# print(df.head())
#
# csvFile = open('editors1.csv', 'w', encoding='utf-8')
# writer = csv.writer(csvFile)
#
# try:
#     for row in table_data:
#         writer.writerow(row)
# finally:
#     csvFile.close()

# --------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

conn = pymysql.connect(host = 'localhost', user='root', passwd='1234', db='scraping', charset='utf8')

cur = conn.cursor()
random.seed(None)

def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES ("%s", "%s")', (title,content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').text
    content = bs.find('div', {'id': 'mw-content-text'}).find('p').text
    store(title,content)
    return bs.find('div', {'id':'bodyContent'}).\
            find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
try:
    while len(links)>0:
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links=getLinks(newArticle)
finally:
    cur.close()
    conn.close()

# --------------------------------------------------------------------