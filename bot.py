import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from valyuta_function import valyuta_determiner

logging.basicConfig(level=logging.INFO)

TOKEN = "6259099877:AAG9x5vtfqFhMtyIEO0qmEfPvl8XapR-2fU"


bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

USD_UZS_Button = KeyboardButton("USD va UZS")
EUR_UZS_Button = KeyboardButton("EUR va UZS")
RUB_UZS_Button = KeyboardButton("RUB va UZS")
selectionButton = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
selectionButton.row(USD_UZS_Button, EUR_UZS_Button, RUB_UZS_Button)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.reply("Hello  welcome to the bot. This bot is an exchange rate bot."
                    "Choose one of the commands to use the bot", reply_markup=selectionButton)


@dp.message_handler(commands=['help'])
async def start(msg: types.Message):
    await msg.reply("Choose one of the commands to use the bot.", reply_markup=selectionButton)


@dp.message_handler(text_contains='USD va UZS')
async def usdValyuta(msg: types.Message):
    valyuta = valyuta_determiner()
    await msg.answer(f"1 Dollar {valyuta} som.")


@dp.message_handler(text_contains='EUR va UZS')
async def eurValyuta(msg: types.Message):
    valyuta = valyuta_determiner('EUR', 'UZS')
    await msg.answer(f"1 EURO {valyuta} som.")


@dp.message_handler(text_contains='RUB va UZS')
async def rubValyuta(msg: types.Message):
    valyuta = valyuta_determiner("RUB", "UZS")
    await msg.answer(f"1 RUB {valyuta} som.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
