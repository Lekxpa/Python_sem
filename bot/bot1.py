from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def msg(update, context):
    file_to_download = await update.message.document.get_file()


    file_path = await file_to_download.download_to_drive()
    
    os.system(f'python {file_path} > {str(file_path)}.out 2> {str(file_path)}.error') # прочитали файл и записали его в файл hello
    
    text_message = None
    with open(str(file_path) +'.out') as f:
        text_message = f.read()

    if text_message == '':
        with open(str(file_path) + '.error') as f:
            text_message = f.read()

    if text_message == '':
        text_message = 'Nothing to output'

    # print(type(file_path))
    # print(file_path)
    await update.message.reply_text(text_message)
    # await update.message.reply_text(str(file_path))
         
# async def callback(update: Update, context: CallbackContext)

app = ApplicationBuilder().token("5803182677:AAE7-5Q2HEEQTEibl1KayeA_IXMrEQsokd4").build()


app.add_handler(MessageHandler(filters.Document.FileExtension("py"), msg))
# app.add_handler(MessageHandler(telegram.ext.filters.ALL, msg))
# telegram.ext.filters.ALL
# app.add.handler(MessageHandler(filters.ALL, msg))
app.add_handler(CommandHandler("hello", hello))
# app.add.handler(MessageHandler(filters.ALL, msg))

app.run_polling()