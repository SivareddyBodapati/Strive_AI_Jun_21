# import telebot
# import os
# API_KEY = os.getenv('API_KEY')
# bot =telebot.TeleBot(API_KEY)
# @bot.message_handler(command=['hello'])
# def hello(message):
#     bot.reply_to(message, "Hey! Hows it going?")

# bot.polling()

from telegram.ext import Updater, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1935052053:AAEZuxWbtWQCMYJp_KcjkQY-hMe6OJ2UCRQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()