from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import spy
# from spy import log

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}\n\
        \nобщежитие слушает! :)\n\
        \nДля работы с Телефонной книгой напишите "/menu" и отправьте сообщение!')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Выберите необходимую команду:\
        \n/search_name\n/add_name\n/look_at_phonebook")



async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(Update,ContextTypes)
    # spy.log
    # await update.message.reply_text(f" See you, {update.effective_user.first_name}")
    dt = update.message.text
    print(dt)
    ls = dt.split() # /sum 2423 89089
    x = int(ls[1])
    y = int(ls[2])
    #  эхо-бот
    # await update.message.reply_text(f'{dt}') 
    await update.message.reply_text(f'{x} + {y} = {x + y}') 

async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f" See you, {update.effective_user.first_name}")