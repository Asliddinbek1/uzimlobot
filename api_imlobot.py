import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord
from imlobot_btn import menu

API_TOKEN = '5255326126:AAHmi_UkDVP_-KSZNdIYKob5t-r7GLOafiw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom - {message.from_user.full_name} -ImloBotga xush kelibsiz", reply_markup=menu)


@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.answer(" @Odamemasbot ga murojaat qiling ")
@dp.message_handler()
async def help_user(message: types.Message):
    word = message.text
    natija = checkWord(word)
    if natija['available']:
        response = f'✅\n togri🤝 \n {word.capitalize()}'
    else:
        response = f"❌ xato ❌ \n oxshash sozlar👇\n   {word.capitalize()}\n "
        for text in natija['matches']:
            response += f"✅ togri🤝 {text.capitalize()}\n"
    await message.answer(response)

@dp.message_handler(regexp='🤖 Boshqa botdan foydalanish')
async def bot(message: types.Message):
    await bot.send_message(message.chat.id,"Shu link orqali oting  '@habib_ilm_bot'",reply_markup=menu)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)