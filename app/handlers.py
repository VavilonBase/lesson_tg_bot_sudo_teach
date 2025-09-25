from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb # имортируем клавиатуру. Будет использоваться только здесь, больше нигде

# Все хендлеры должны хранится отдельно
# Но как притянуть диспетчер и сообщать aiogram-у, что хендлеры находятся тут? Нужен роутер
router = Router()

# Декоратор, является диспетчером и говорит о том, что диспетчер ждем сообщение
# CommandStart - говорит о том, что бот ждем команду start
# Называется Handler
@router.message(CommandStart())
async def cmd_start(message: Message):
    # answer - бот просто пишет сообщение
    #await message.answer(f'Привет!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')
    # reply - бот отвечает на сообщение
    await message.reply(f'Привет!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',
                        # reply_markup=kb.main # Добавляем кнопки в обработчик start, но можно прицепить к любому сообщению
                        # reply_markup=kb.settings # К одному сообщению можно прицепить только одну клавиатуру
                        #reply_markup=await kb.reply_cars()
                        reply_markup=await kb.inline_cars()
                        )

# Command - позволяет фильтровать любые комманды, которые мы вводим, а не только start
@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

# F - maginc fillter. Позволяет задать текст, который мы хотим получить
@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('Все зашибись')

# С помощью F фильтра можно ловить все, фото, стикеры, локации, фотографии и т.д.
@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

# Можно отправлять фото пользователю
@router.message(Command('put_photo'))
async def put_photo(message: Message):
    # Можно и отправить фото по ссылке, просто вместо id будет url
    await message.answer_photo(photo = 'AgACAgIAAxkBAAMkaI0gmr6KGZ_Cj54Q-ZpHnlbGN2sAAhv0MRvUZXBI0m37K8Rn0p8BAAMCAAN5AAM2BA',
                               caption = 'Просто картинка')
