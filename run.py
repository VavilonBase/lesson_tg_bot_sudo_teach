import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN

from app.handlers import router

# Бот принимает токен и инициализирует подключение к нему
# Можно создать несколько ботов
# Токен не стоит хранить тут, надо перенести в переменные окружения или, например, в другой файл, который не будет выкладываться в гит
bot = Bot(token = TOKEN)

# Является основным роутером. Работа происходит через него, либо же в него передаются другие роутеры
dp = Dispatcher()


async def main():
    # Импортируем роутер из хендлеров
    dp.include_router(router)

    # Эта функция отправляет запрос на сервера телеграмм, если ответ есть - то она его обработает, 
    # если ответа нет, то ожидаем ответ от телеграмма
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Добавляем логирование
    logging.basicConfig(level=logging.INFO)

    # try except, чтобы при выключении бота не было KeyboardInterrupt (после нажатия CTRL + C)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')