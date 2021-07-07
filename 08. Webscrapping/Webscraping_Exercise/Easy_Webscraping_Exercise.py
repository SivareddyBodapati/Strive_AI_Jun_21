#importing, Dictionary iniialization and scarapping url
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

dict = { }
url = "https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996"
sfwpage = requests.get(url)
sfwsoup = BeautifulSoup(sfwpage.content, "html.parser")

#finding labels for days of the week, e.g " wedesnesday" , etc
sevendaylist = sfwsoup.find('div', id='detailed-forecast-body')
allrows = sevendaylist.find_all('div')
listofdays = []
for r in range(30):
    labels = allrows[r].find_all('div', class_="col-sm-2 forecast-label")
    for label in labels:
        listofdays.append(label.text)

# scraping the description  .range
weatherdesc = []
for r in range(30):
    description = allrows[r].find_all('div', class_="col-sm-10 forecast-text")
    for desc in description:
        weatherdesc.append(desc.text)

def convert(x):
    return round(((float(x) - 32) * 5.0/9.0), 2)

highlowtemp = []
boxtemp = sfwsoup.find('ul', id='seven-day-forecast-list')
highlows = boxtemp.find_all('p', class_="temp")
for temp in highlows:
    highlowtemp.append(temp.text)
highlowtemp.append('Low: 56 °F')

incelsius = []
for temp in highlows:
    temp = temp.text
    temp = temp.split()
    x = (float(temp[1]))
    incelsius.append((convert(x)))

incelsius.append((convert(56)))

Dates = ["07/7/2021","07/7/2021","08/7/2021","08/7/2021","09/7/2021","09/7/2021","10/7/2021","10/7/2021","11/7/2021","11/7/2021"]
dict["dayofweek"] = listofdays
dict['date'] = Dates
dict["description"] = weatherdesc
dict['high/low'] = highlowtemp
dict['in °C'] = incelsius


df =pd.DataFrame(dict)

print(df)


