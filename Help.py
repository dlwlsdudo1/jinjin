# 예제 3-38 라이브러리 추가하기
from selenium import webdriver 
from bs4 import BeautifulSoup 
import time
import pandas as pd


driver = webdriver.Chrome("C:/drive/chromedriver")
driver.get("https://playboard.co/")
time.sleep(3)
driver.implicitly_wait(2)
# elem = driver.find_element_

btn_search = driver.find_element_by_css_selector("#app > div.__window > div > div > div.home__charts > div > div > div:nth-child(1) > section:nth-child(1) > a > svg")
btn_search.click()
time.sleep(3)
driver.implicitly_wait(2)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
print("-----1-----")
boxItems = soup.select("tbody > chart__row")
print("-----2-----")
print(boxItems)
print("-----3-----")

try:

    for boxItem in boxItems:
    

        asd = boxItem.text       
        # asd = boxItem.select_one("td.name > a")
        # k = re.sub('<.*?>','',asd
        print(asd)
        # print(k)
        if asd != "":
            qwe = boxItem.find("a")['title']
            print(qwe)

        

except Exception as e:
    print("페이지 파싱 에러", e)
finally:
    time.sleep(3)
    driver.close()
