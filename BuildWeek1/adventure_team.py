import selenium
from selenium import webdriver
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
# import seaborn as sns


#variables
title_list = []
year_list = []
ratings_list = []
tot_metascore = []
director_list = []
tot_votes = []
tot_gross = []
tot_genre = []
tot_duration = []
actor_list1 = []
actor_list2 = []
actor_list3 = []
actor_list4 = []


for it in range(0,2):
    url = "https://www.imdb.com/search/title/?title_type=feature&genres=adventure&sort=num_votes,desc&start=" + str(1+50*it) + "&explore=genres&ref_=adv_nxt"

    #driver relative path
    my_driver = "chromedriver.exe"

    #loading driver with url
    driver = webdriver.Chrome(executable_path=r'C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    sleep(3)


    n = 51

    #title

    for i in range(1,n):
        title = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/h3/a')
        title_list.append(title.text)
    # print(title_list)

    #year

    for i in range(1,n):
        year = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/h3/span[2]')
        year_list.append(year.text)
    # print(year_list)

    #rating

    for i in range(1,n):
        ratings = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/div/div[1]/strong')
        ratings_list.append(ratings.text)
    # print(ratings_list)

    #meta score

    metascore_50 = driver.find_elements_by_xpath('//div[@class="inline-block ratings-metascore"]')
    for row3 in metascore_50:
        tot_metascore.append(row3.text)
    # print(len(tot_metascore))

    #Director

    for i in range(1,n):
        director = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[3]/a[1]')
        director_list.append(director.text)
    # print(director_list)

    #film stars


    for i in range(1,n):
        for j in range(2,6):
            films = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div['+str(i)+']/div[3]/p[3]/a['+str(j)+']')
            if j == 2:
                actor_list1.append(films.text)
            elif j == 3:
                actor_list2.append(films.text)
            elif j == 4:
                actor_list3.append(films.text)
            else:
                actor_list4.append(films.text)

    #votes

    for i in range(1,n):
        stars = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/div/div[1]/strong')
        tot_votes.append(stars.text)
    # print(tot_votes)

    #gross

    for i in range(1,n):
        gross = driver.find_element_by_xpath('//html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[4]/span[5]')
        #print(type(title),title)
        #print(title.text)
        tot_gross.append(gross.text)
    # print(tot_gross)

    #description

    # descript_50 = driver.find_elements_by_xpath('//p[@class="text-muted"]')
    # for row_d in descript_50:
    #     tot_description.append(row_d.text)
    # print(len(tot_description))

    #genre

    genre_50 = driver.find_elements_by_xpath('//span[@class="genre"]')
    for row in genre_50:
        tot_genre.append(row.text)
    # print(tot_genre)

    # duration

    duration_50 = driver.find_elements_by_xpath('//span[@class="runtime"]')
    for row1 in duration_50:
        tot_duration.append(row1.text)
    # print(tot_duration)

# print(len(title_list))
# print(len(year_list))
# print(len(ratings_list))
# print(len(tot_metascore))
# print(len(director_list))
# print(len(tot_votes)) 
# print(len(tot_gross)) 
# print(len(tot_genre))
# print(len(tot_duration))
# print(len(actor_list1))
# print(len(actor_list2))
# print(len(actor_list3))
# print(len(actor_list4))

tot_metascore1= []
tot_duration1=[]

data = {'Title' : title_list, 'Year' : year_list, 'Ratings' : ratings_list,
        'Director' : director_list,'Metascore' : tot_metascore1,'Votes' : tot_votes , 'Gross':tot_gross,
        'Genre':tot_genre , 'Duration':tot_duration1,
        'Actor 1' : actor_list1, 'Actor 2' : actor_list2,
        'Actor 3' : actor_list3, 'Actor 4' : actor_list4 
        }


for i in range(0,100):
    tot_metascor=tot_metascore[i].split('M')
    tot_duratio = tot_duration[i].split('m')
    tot_duration1.append(tot_duratio[0])
    tot_metascore1.append(tot_metascor[0])

df = pd.DataFrame(data)
plt.plot(df['Duration'],df['Metascore'])

