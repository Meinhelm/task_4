from aiogram import types
from but_handler import dp
from SQL import SQLighter
db = SQLighter('db.db')
@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.reply("Привет, ты можешь подписаться с помощью команды /subscribe, а если хочешь узнать больше то введи /info")
@dp.message_handler(commands=['info'])
async def start(message:types.Message):
    await message.reply('Команды:/start,/info,/subscribe,/unsubscribe,/news')
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        #Если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id, True)
    else:
        #Если он уже есть в базе то обновляем статус подписки
        db.update_users(message.from_user.id, True)

    await message.answer("Вы подписались")
#Команда отписки
@dp.message_handler(commands = ['unsubscribe'])
async def unsubscribe(message: types.Message):
    if(db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе , то запоминаем его
        db.update_users(message.from_user.id, False)
        await message.answer("Вы отписались")
    else:
        #если его он есть в бд, то обновляем статус
        db.update_users(message.from_user.id, False)
        await message.answer("Вы и так не подписаны")


if __name__ == '__main__':
    from aiogram import executor
    from but_handler import dp
    executor.start_polling(dp)
