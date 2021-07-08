import selenium
from selenium import webdriver
import pandas as pd
from time import sleep
url ="https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c"
my_driver = "chromedriver.exe"
# driver = webdriver.Chrome(my_driver)
driver = webdriver.Chrome(executable_path=r'C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(url)

sleep(3)
dict = { }
day= []
date=[]
temp =[]
temp1 =[]
daily_content=[]
description =[]
ltem =[]
days = driver.find_elements_by_xpath('//h2[@class="DetailsSummary--daypartName--3C7r4"]')
for r in days:
    day.append(r.text+"/07/2021")

High_temp = driver.find_elements_by_xpath('//span[@class="DetailsSummary--highTempValue--3neDD"]')
for t in High_temp:
    temp.append(t.text)

Low_temp = driver.find_elements_by_xpath('//span[@class="DetailsSummary--lowTempValue--2wKBA" ]')
for l in Low_temp:
    temp1.append(l.text)  

day[0] = driver.find_element_by_xpath('//span[@class="DailyContent--daypartDate--LLcW2"]').text+"/07/2021"
tem= driver.find_elements_by_xpath('//span[@class="DailyContent--temp--3VpIL"]')
for t1 in range(2):
    ltem.append(tem[t1].text)
    
# temp1[0] = driver.find_element_by_xpath('//span[@class="DailyContent--temp--3VpIL" ]').text
temp[0] = ltem[0]
temp1[0] = ltem[1]
# .replace("°", "")(-32*(5/9))
# '//a[@class="a-link-normal a-text-normal"]'
# for price in laptop_price:
#     print(price.text)
# print(day[:10])
dict["dayofweek"] = day[:10]
dict["highTemp"] = temp[:10]
dict["LowTemp"] = temp1[:10]
df =pd.DataFrame(dict)
print(df)