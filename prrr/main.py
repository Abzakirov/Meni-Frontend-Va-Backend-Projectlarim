from aiogram import Dispatcher, Bot, filters, types, F
import asyncio

bot = Bot(token="7275656876:AAH_2NYk0n5VYTcqmlgnH3y1MAHilWese1E")
dp = Dispatcher(bot=bot)


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer("Добро пожаловать")


@dp.message(F.text)
async def echo_function(message: types.Message):
    await message.answer(message.text)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())