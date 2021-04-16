from aiogram import Bot, Dispatcher, types
import logging
import config

bot = Bot(token=config.API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,)
