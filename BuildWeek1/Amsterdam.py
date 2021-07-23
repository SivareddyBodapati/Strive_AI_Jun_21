import selenium
from selenium import webdriver
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt

url ="https://www.yelp.de/search?find_desc=Hotel&find_loc=amsterdam"
driver = webdriver.Chrome(executable_path=r'C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(url)
sleep(3)
Hotel_list = []
Resta_list = []
vec_list = []
# /html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a/font/font
n=13
# for i in range(3,n):
for i in range(3,n):
    title = driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[' +str(i)+ ']/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')
    Hotel_list.append(title.text)

rest=driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/a/span[1]')
rest.click()
sleep(3)
for i in range(3,n):
      title1 = driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[' +str(i)+ ']/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')
      Resta_list.append(title1.text)
sleep(2)
car=driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div/a/span[1]')
car.click()
sleep(3)
for i in range(3,n):
      title2 = driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[' +str(i)+ ']/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a')
      vec_list.append(title2.text)

# print(Resta_list)       
data = {'Hotels' : Hotel_list, 'Restaurants' : Resta_list, 'car_rental' : vec_list
        }
df = pd.DataFrame(data)
print(df)
