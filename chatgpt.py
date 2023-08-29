import openai
import telebot
import urllib.request
import os
from telebot import types

token = "6070799258:AAHqxPvWpT1upaA6RN3gfbstczxjwfr7IIM"
API_KEY = "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"

openai.api_key = API_KEY
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['image'])
def image_message(message):
    print("Yes")
    try:
        i = 1
        if message.text[7]>'0' and message.text[7]<='9':
            i = int(message.text[7])
        image_url = openai.Image.create(
            prompt=message.text[7:],
            n=i,
            size="1024x1024")
        mass = []
        ii = 0
        while ii<i:
            mass.append(telebot.types.InputMediaPhoto(image_url.data[ii].url))
            ii=ii+1
        bot.send_media_group(message.chat.id, mass)
    except:
        bot.send_message(message.chat.id, "Цензура")

@bot.message_handler(commands=['start'])
def image_message(message):
    bot.send_message(message.chat.id, "Иди нахуй")

@bot.message_handler(commands=['bot'])
def start_message(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.text[4:]}])
    mes = completion.choices[0].message.content
    i = 0
    while i<len(mes)-i:
        bot.send_message(message.chat.id, mes[i:i+4000])
        i=i+4000
        

bot.infinity_polling()


