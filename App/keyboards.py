from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                            [KeyboardButton(text='Корзина')],
                            [KeyboardButton(text='Контакты'),
                            KeyboardButton(text='О Нас')]],
                            resize_keyboard=True,
                            input_field_placeholder= 'Выберите один из пунктов...')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "Супы", callback_data='Soup')],
    [InlineKeyboardButton(text='Первое', callback_data='First')],
    [InlineKeyboardButton(text='Второе', callback_data='Second')]])

getnumber = ReplyKeyboardMarkup(keyboard =[[KeyboardButton(text='Скинуть номер телефона', 
                                                           request_contact=True)]], resize_keyboard=True)

start2 = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = 'Открыть вк', web_app= WebAppInfo(url = 'https://vk.com/feed') )]])
