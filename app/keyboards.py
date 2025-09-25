from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Есть два вида клавиатуры
# 1) Reply
# Выходит в самом низу, вместо обычной клавиатуры
# При нажатии reply кнопки ее содержимое отправляется в чат
# Так же reply кнопки могут запрашивать локацию, контакты или какие-то другие данные

# 2) Inline
# Кнопки, которые цепляются за сообщения
# При нажатии inline кнопки ничего не отправляется в чат. 
# Так же inline кнопки могут запрашивать локацию, контакты или какие-то другие данные
# А при нажатии на inline на сервер отправляется какой-то запрос (callback) и мы получаем ответ. То есть срабатывает какая-то функция, которую не видит пользователь
# При нажатии на inline мы может открывать ссылку или miniapp

# Создаем reply клавиатуру
main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Каталог')], # Ряд
    [KeyboardButton(text = 'Корзина'), KeyboardButton(text = 'Контакты')]
],  resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...')


# Создаем inline кнопки
# По созданию идентичны с reply. Так же ряды
settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Youtube', # Помимо текста надо обязательно добавить что-то еще
                          url='https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4')]
])

# Builder
# Допустим мы получаем список автомобилей
# Значения динамические, допустим мы достали их из БД
cars = ['Tesla', 'Mercedes', 'BMW', 'Porsche']

async def reply_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    
    # as_markup - обязательно
    return keyboard.adjust(2).as_markup() #adjust - для размера клавиватуры, точнее сколько в одном ряду будет кнопок

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, 
                                          url='https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4'))
    
    # as_markup - обязательно
    return keyboard.adjust(3).as_markup() #adjust - для размера клавиватуры, точнее сколько в одном ряду будет кнопок