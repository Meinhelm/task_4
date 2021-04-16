import logging
import SQL
from aiogram.dispatcher.filters import Command
from aiogram.types import Message , CallbackQuery
from callback_datas import read_callback
from choice_buttons import choice, sport_keyboard, science_keyboard, weather_keyboard, all_keyboard
from loader import dp

@dp.message_handler(Command("news"))
async def show_news(message: Message):
    await message.answer(text="Выбирите категорию новостей", reply_markup=choice)
@dp.callback_query_handler(text_contains="Sport")
async def reading_sport(call:CallbackQuery):
    await call.answer(cache_time=3)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Вы выбрали категорию спорт", reply_markup=sport_keyboard)
@dp.callback_query_handler(read_callback.filter(news_name="science"))
async def reading_science(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=3)
    logging.info(f"call={callback_data}")
    await call.message.answer(f"Вы выбрали категорию наука", reply_markup=science_keyboard)
@dp.callback_query_handler(read_callback.filter(news_name="weather"))
async def reading_weather(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=3)
    logging.info(f"call={callback_data}")
    await call.message.answer(f"Вы выбрали категорию погода", reply_markup=weather_keyboard)
@dp.callback_query_handler(read_callback.filter(news_name="political"))
async def reading_political(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=3)
    logging.info(f"call={callback_data}")
    await call.message.answer(f"Вы выбрали категорию политика", reply_markup=science_keyboard)
@dp.callback_query_handler(text="return")
async def return_menu(call:CallbackQuery):
    await call.answer("Вы вернулись в главное меню", show_alert=True)
    await call.message.edit_reply_markup()

@dp.callback_query_handler(read_callback.filter(news_name="all"))
async def reading_all(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=3)
    logging.info(f"call={callback_data}")
    await call.message.answer(f"Вы выбрали список всех новостей", reply_markup=all_keyboard)
