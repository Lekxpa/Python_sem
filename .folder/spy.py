from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text(f"{datetime.datetime.now().time()}")
    file = open('dates.csv', 'a', encoding = 'utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}')
    file.close()
