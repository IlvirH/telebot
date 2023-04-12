import os
import logging

from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# admin_id

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hello, {user_name}!'
    logging.info(f'{user_name} {user_id} send message: {message.text}')
    await message.reply(text)

trnslt = {'А': 'A', 'Б': 'B', 'В': 'V','Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', \
          'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', \
          'С' : 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'TCH', 'Ш': 'SH', \
          'Щ': 'SHCH', 'Ь': '','Ы': 'Y', 'Ъ': 'IE', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA'}

@dp.message_handler()
async def send_translate(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    result = ''.join([trnslt[i] if ord(i) in range(1040, 1104) else i for i in text.upper()])
    logging.info(f'{user_name} {user_id} send message: {result}')
    await bot.send_message(user_id, result)
    # await bot.send_message(admin_id, ''.join([trnslt[i] for i in text]))


if __name__ == '__main__':
    executor.start_polling(dp)


