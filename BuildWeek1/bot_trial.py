import telebot
from telegram.ext import *
from datetime import  datetime
import selenium
from selenium import webdriver
from time import sleep
import pandas as pd
import numpy as np

transcripts =[]
views =[]
likes = []
dis_likes =[]
Title =[]
length = []
coments=[]
description =[]

my_driver = "chromedriver.exe"
def london(url):
    # un comment the first driver for relative path and comment the second driver
    # driver = webdriver.Chrome(my_driver)
    driver = webdriver.Chrome(executable_path=r'C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe')
    
    # url="https://www.youtube.com/watch?v=YXN_lNZZAZA&ab_channel=Kontor.TV"
    # url="https://www.youtube.com/watch?v=6LD30ChPsSs&ab_channel=ThinkMusicIndia"
    # url = "https://www.youtube.com/watch?v=_TFribViDSs&ab_channel=AshStudio7"
    driver.get(url)

    # beautiful soup
    # sfwpage = requests.get(url)
    # sfwsoup = BeautifulSoup(sfwpage.content, "html.parser")

    sleep(2)

    # accept the cookies 
    cookies = driver.find_element_by_xpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button')
    cookies.click()
    
    sleep(1)
    stop_play = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[1]/video')
    stop_play.click()

    sleep(2)

    # no of video views 
    view=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/ytd-video-view-count-renderer/span[1]')
    views.append(view.text)
    # no of video likes 
    like =driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-formatted-string')
    likes.append(like.text)
    # no of video dislikes 
    dis_like =driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-formatted-string')
    dis_likes.append(dis_like.text)
    # title of the video 
    title =driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string')
    Title.append(title.text)
    # length of the video
    len_video = driver.find_element_by_xpath('//span[@class="ytp-time-duration"]')
    length.append(len_video.text)
    # description of the Link
    desc = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[7]/div[2]/ytd-video-secondary-info-renderer/div/ytd-expander')
    description.append(desc.text)
    # no of comments for the video
    # coment = driver.find_element_by_xpath('//*[@id="count"]/yt-formatted-string/span[1]')
    # coments.append(coment.text)
    # print(coments)

    sleep(2)
    # to open the  transcripts
    dots=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/yt-icon-button/button/yt-icon')
    dots.click()
    
    sleep(1)
    # to check whether the video has transcription or not!
    check_trans = driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer").text
    
    # print(check_trans)
    if 'transcript' in check_trans:
        # print('Yes! It has transcript')
        sleep(1)
        trans=driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer/tp-yt-paper-item/yt-formatted-string')
        trans.click()
        sleep(1)
        # timestamps of the transcripts
        dots_trans = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer/div[1]/ytd-engagement-panel-title-header-renderer/div[2]/div[5]/ytd-menu-renderer/yt-icon-button/button/yt-icon')
        dots_trans.click()
        sleep(1)
        timestamps = driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer/tp-yt-paper-item/yt-formatted-string')
        timestamps.click()
        sleep(1)
        # transcription adding to the empty list
        trans_desc =driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer/div[2]/ytd-transcript-renderer/div[1]")
        transcripts.append(trans_desc.text)
        data ={'Title':Title,'Likes':likes,'Dis_Likes':dis_likes,'No_Of_Views':views,'Transcripts':transcripts,'Video_length':length,'Description':description}
        return f"Title:{Title}\n\nLength: {length} mins \n\nViews: {views} Views\n\nLikes: {likes} Likes\n\nDislikes: {dis_likes} Dislikes\n\n\nDescription:\n\n{description}\n\nYes! It has transcript\n\n\nTranscription:\n\n {transcripts}\n\n"
    if 'transcript' not in check_trans:
        # print('no! It has no transcript')
        data ={'Title':Title,'Likes':likes,'Dis_Likes':dis_likes,'No_Of_Views':views,'Video_length':length,'Description':description}
        return f"Title:{Title}\n\nLength: {length} mins \n\nViews: {views} Views\n\nLikes: {likes} Likes\n\nDislikes: {dis_likes} Dislikes\n\n\nDescription:\n\n{description}\n\n\nNo! It has no transcript"
    #  to stop the video

   
    
    # df = pd.DataFrame(data)
    # df['No_Of_Views'] = df['No_Of_Views'].str.replace('views', '')
    # print(df)
    # adding to the csv file
    # df.to_csv("Name of the file1.txt")
    # print(coments)
    return 'the link is invalid'


def sample_response(input_text):
	user_message = str(input_text).lower()

	if user_message in ("hello","hi", "sup"):
		return "Hey! How's it going?"
	if user_message in ("who are you", "who are you?"):
		return "I am siva3244 Bot!"
	if user_message in ("time", "time?"):
		now =datetime.now()
		date_time = now.strftime("%d/%m/%y, %H:%M:%S")
		return str(date_time)

	return "I don't understand you."

print('Bot started .....')

def start_command(update, context):
	update.message.reply_text('Type something random to get started!')

def help_command(update, context):
	update.message.reply_text('If you need help! You should ask for it on Google!')

def handle_message(update, context):
    
	text =str(update.message.text).lower() #recieves input from the user
	response =sample_response(text) #process the input
	update.message.reply_text(response) #gives back to user

def handle_message_1(update, context):
	text =str(update.message.text).lower() #recieves input from the user
	# response =sample_response(text) #process the input
	url=update.message.text
	response =london(url)
	update.message.reply_text("just wait for few seconds to get the document file") #gives back to user

def error(update, context):
	print(f"Update {update} caused error {context.error}")

API_KEY ='1918596628:AAExXRMBPjarHxN1DuZL3Jdgmm_ifAqeWQ4'
def main():
	updater =Updater(API_KEY, use_context =True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))
    
	dp.add_handler(MessageHandler(Filters.text, handle_message_1))
	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()


main()