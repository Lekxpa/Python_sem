from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import command_bot
# import spy

app = ApplicationBuilder().token("5803182677:AAE7-5Q2HEEQTEibl1KayeA_IXMrEQsokd4").build()

app.add_handler(CommandHandler("hello", command_bot.hello))
app.add_handler(CommandHandler("time", command_bot.time))
app.add_handler(CommandHandler("help", command_bot.help))
app.add_handler(CommandHandler("sum", command_bot.sum))
app.add_handler(CommandHandler("bye", command_bot.bye))
# app.add_handler(CommandHandler("log", spy.log))

app.run_polling()

# t.me/Test_gb_lekbot