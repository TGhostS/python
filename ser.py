import datetime
import json

import keyboard
import openpyxl
import telebot
from openpyxl import load_workbook

#инлайновые кнопки при входе
from telebot import types

token = "1327620351:AAFuPqqT81BgTp0vaw7dzP1UvgENEUltJHo"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def inline(message):
  key = types.InlineKeyboardMarkup()
  but_1 = types.InlineKeyboardButton(text="Запись к врачу", callback_data="Запись к врачу")
  but_2 = types.InlineKeyboardButton(text="Получение направления", callback_data="Получение направления")
  but_3 = types.InlineKeyboardButton(text="Просмотр рейтинга и отзывов врачей", callback_data="Просмотр рейтинга и отзывов врачей")
  but_4 = types.InlineKeyboardButton(text="Выйти", callback_data="Выйти")
  key.add(but_1, but_2, but_3, but_4)
  bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=key)


@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'Запись к врачу':
        bot.send_message(c.message.chat.id, 'Это кнопка 1')
    if c.data == 'Получение направления':
        bot.send_message(c.message.chat.id, 'Это кнопка 2')
    if c.data == 'Просмотр рейтинга и отзывов врачей':
        bot.send_message(c.message.chat.id, 'Это кнопка 3')
    if c.data == 'Выйти':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Зарегистрироваться', 'Войти')
        bot.delete_message(c.message.chat.id, c.message.message_id)

bot.polling()