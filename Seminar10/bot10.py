from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
# import token

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}\n\
        \nобщежитие слушает! :)\n\
        \nДля работы с Телефонной книгой напишите "/menu" и отправьте сообщение!')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Выберите необходимую команду:\
        \n/search_name\n/add_name\n/look_at_phonebook")

async def search_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = await update.message.reply_text(f'Введите значение, которое необходимо найти: \n')
    print(t)
    os.system("python actions_search.py")
    

async def add_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    os.system("python view_add_hand.py")
    await update.message.reply_text(f"add")

async def look_at_phonebook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('Phonebook.md', 'rb')
    send_document(chat_id, file)
    # os.system("python actions_show.py")
    await update.message.reply_text(f"look_at")


async send_document(chat_id, document, caption=None, disable_notification=None, reply_to_message_id=None, 
reply_markup=None, parse_mode=None, thumb=None, disable_content_type_detection=None, allow_sending_without_reply=None, 
caption_entities=None, protect_content=None, message_thread_id=None, *, filename=None, read_timeout=None, write_timeout=20, 
connect_timeout=None, pool_timeout=None, api_kwargs=None)
    # @bot.message_handler(content_types=["text"])
    # def text(message):
        # if message.text == 'document':
        #     file = open('file.txt', 'rb')
            # bot.send_document(message.chat.id, file)



# async def msg(update, context):
#     file_to_download = await update.message.document.get_file()

#     file_path = await file_to_download.download_to_drive()
    
#     os.system(f'python {file_path} > {str(file_path)}.out 2> {str(file_path)}.error') # прочитали файл и записали его в файл hello
    
#     text_message = None
#     with open(str(file_path) +'.out') as f:
#         text_message = f.read()

#     if text_message == '':
#         with open(str(file_path) + '.error') as f:
#             text_message = f.read()

#     if text_message == '':
#         text_message = 'Nothing to output'
    # await update.message.reply_text(text_message)



    # print(type(file_path))
    # print(file_path)
    
    # await update.message.reply_text(str(file_path))


# async def callback(update: Update, context: CallbackContext)

app = ApplicationBuilder().token("5803182677:AAE7-5Q2HEEQTEibl1KayeA_IXMrEQsokd4").build()


# app.add_handler(MessageHandler(filters.Document.FileExtension("py"), msg))

# app.add_handler(MessageHandler(telegram.ext.filters.ALL, msg))
# telegram.ext.filters.ALL
# app.add.handler(MessageHandler(filters.ALL, msg))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("search_name", search_name))
app.add_handler(CommandHandler("add_name", add_name))
app.add_handler(CommandHandler("look_at_phonebook", look_at_phonebook))

# app.add.handler(MessageHandler(filters.ALL, msg))

app.run_polling()