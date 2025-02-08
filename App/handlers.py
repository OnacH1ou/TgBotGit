from aiogram import Dispatcher, Bot, F, Router

from aiogram.types import Message, CallbackQuery, WebAppInfo
from aiogram.filters import CommandStart,Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import App.keyboards as kb

router = Router()


class Reg(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Вы нажали старт, я вас поздравляю', reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на помощь, чем я могу вам помочь?')

@router.message(F.text == 'Каталог')
async def Catalog(message: Message):
    await message.answer("Выберите категорию блюда",reply_markup = kb.catalog) 

@router.callback_query(F.data.contains('Soup'))
async def soup(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию супов', show_alert=True)
    await callback.message.answer('Вы выбрали категорию супов')
    
@router.message(Command('reg'))
async def reg(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше Имя')

@router.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.age)
    await message.answer('Введите ваш возраст')

@router.message(Reg.age)
async def reg_age(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите свой номер телефона', reply_markup= kb.getnumber)
    
@router.message(Reg.number,F.contact)
async def contact(message: Message, state: FSMContext):
     await state.update_data(number=message.contact.phone_number)
     data = await state.get_data()
     await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nВаш номер телефона: {data["number"]}')
     await state.clear()


@router.message(Command('start2'))
async def statr2(message: Message):
    await message.answer('Отослал тебе кнопку',reply_markup = kb.start2)