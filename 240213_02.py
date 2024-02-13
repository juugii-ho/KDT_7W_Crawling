# from time import sleep
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome()
# driver.get('https://www.naver.com')
# print(driver.current_url)
#
# sleep(2)
# driver.close()
# driver.quit()

# --------------------------------------------------------------------
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get('https://www.google.com')
#
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source)
#
# driver.implicitly_wait(time_to_wait=5)
# driver.close()
# driver.quit()

# --------------------------------------------------------------------
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
# driver.implicitly_wait(5)
#
# name = driver.find_element(By.CLASS_NAME, "green")
# print(name.text)
#
# print('-'*20)
#
# nameList = driver.find_elements(By.CLASS_NAME, 'green')
# for name in nameList:
#     print(name.text)
#
# driver.quit()

# --------------------------------------------------------------------


# --------------------------------------------------------------------


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# agent_option = webdriver.ChromeOptions()
# user_agent_string = 'Mozilla/5.0'
# agent_option.add_argument('user-agent=' + user_agent_string)
#
# driver = webdriver.Chrome(options=agent_option)
# driver.get('http://nid.naver.com/nidlogin.login')
#
# driver.implicitly_wait(25)
#
# driver.find_element(By.NAME, 'id').send_keys('id')
# driver.find_element(By.NAME, 'pw').send_keys('pw')
#
# driver.find_element(By.ID, 'log.login').click()
#
# driver.quit

# --------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get('https://google.com')
#
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('Python')
# search_box.submit()
#
# time.sleep(3)
# search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
# print(len(search_results))
#
# for result in search_results:
#     title_element = result.find_element(By.CSS_SELECTOR, 'h3')
#     title = title_element.text.strip()
#     print(f"{title}")
#
# driver.quit()


# --------------------------------------------------------------------

# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://blog.naver.com/swf1004/221631056531')
#
# driver.switch_to.frame('mainFrame')
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# whole_border = soup.find('div', {'id':'whole-border'})
# results = whole_border.find_all('div', {'class':'se-module'})
#
# result1=[]
#
# for result in results:
#     print(result.text.replace('\n', ''))
#     result1.append(result.text)

# --------------------------------------------------------------------

# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.coffeebeankorea.com/store/store.asp')
#
# driver.execute_script('storePop2(1)')
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# print(soup.prettify())

# --------------------------------------------------------------------
#
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.coffeebeankorea.com/store/store.asp')
#
# driver.execute_script('storePop2(1)')
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# store_names = soup.select('div.store_txt > p.name > span')
# store_name_list = []
# for name in store_names:
#     store_name_list.append(name.get_text())
#
# print('매장 개수: ', len(store_name_list))
# print(store_name_list)
#
# store_addresses = soup.select('p.addr > span')
# store_address_list = []
# for addr in store_addresses:
#     print(addr.get_text())
#     store_address_list.append(addr.get_text())
#
# driver.quit()


#--------------------------------------------------------

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time


def coffeebean_store(store_list):
    coffeebean_url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver = webdriver.Chrome()

    for i in range(1,388):
        driver.get(coffeebean_url)
        time.sleep(1)

        driver.execute_script('storePop2(%d)' % i)
        time.sleep(1)

        try:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            store_name = soup.select_one('div.store_txt > h2').text
            store_info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
            store_address_list = list(store_info[2])
            store_addr = store_address_list[0]
            store_phone = store_info[3].text
            print('{}{}{}'.format(i+1, store_name, store_addr, store_phone))
            store_list.append([store_name, store_addr, store_phone])
            print(i)
        except:
            continue

def main():
    store_info=[]
    coffeebean_store(store_info)
    coffeebean_table = pd.DataFrame(store_info, columns=('매장이름', '주소', '전화번호'))
    print(coffeebean_table.head())

    coffeebean_table.to_csv('coffeebean_branches.csv', encoding='utf-8', mode='w', index=True)

    print('완료')

main()