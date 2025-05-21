import telebot
import os
from functions import generate

bot = telebot.TeleBot("7746221281:AAHX5sufyo8nGWbkZHRJFJoobrF253g181I")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salom men SNRG AI botman" )

@bot.message_handler(func=lambda message: True)
def javob_qaytarish(message):
    user_input = message.text
    print("priyom!")
    response = generate(user_input)
    bot.send_message(message.chat.id, response)

print("Bot ishga tushdi")
bot.polling()
    