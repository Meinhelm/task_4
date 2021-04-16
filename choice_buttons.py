from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import read_callback
from config import URL_Sport, URL_Science, URL_Political, URL_Weather, URL_All

choice = InlineKeyboardMarkup(row_width=2)

Sport_news = InlineKeyboardButton(text="Спорт", callback_data=read_callback.new(news_name="Sport",quantity=10))
choice.insert(Sport_news)
Science_news = InlineKeyboardButton(text="Наука", callback_data="read:science:10")
choice.insert(Science_news)
Political_news = InlineKeyboardButton(text="Политика", callback_data="read:political:10")
choice.insert(Political_news)
Weather_news = InlineKeyboardButton(text="Погода", callback_data="read:weather:10")
choice.insert(Weather_news)
Return_but = InlineKeyboardButton(text= "Вернуться в главное меню", callback_data="return")
choice.insert(Return_but)
All_news = InlineKeyboardButton(text="Новости за сегодня", callback_data="read:all:10")
choice.insert(All_news)
sport_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[

    [
        InlineKeyboardButton(text='читай тут', url=URL_Sport)

    ]
    ]
)

science_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[

    [
        InlineKeyboardButton(text='читай тут', url=URL_Science)
    ]
    ]
)
political_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[

    [
        InlineKeyboardButton(text='читай тут', url=URL_Political)
    ]
    ]
)
weather_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[

    [
        InlineKeyboardButton(text='читай тут', url=URL_Weather)
    ]
    ]
)
all_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[

    [
        InlineKeyboardButton(text='читай тут', url=URL_All)
    ]
    ]
)