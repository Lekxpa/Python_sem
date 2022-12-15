# import asyncio *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
# from actions_search import search
# from aiogram.types import InputFile, Message
# from os import SendfileNotAvailableError
# import token
# import logging

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!\n\
        \nОбщежитие слушает! :)\n\
        \nДля работы с Телефонной книгой напишите "/menu" и отправьте сообщение!')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Выберите необходимую команду:\
        \n/sum\n/add_name\n/look_at_phonebook")


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

# async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # dt = await update.message.reply_text(f'Введите значение, которое необходимо найти: \n')

#     dt = update.message.text
#     print(dt)
#     ls = dt.split() # /sum 2423 89089
#     x = int(ls[1])
#     y = int(ls[2])
#     #  эхо-бот
#     # await update.message.reply_text(f'{dt}') 
#     await update.message.reply_text(f'{x} + {y} = {x + y}') 

# #     dt = update.message.text
# #     print(dt)
# #     lt = dt.split() # /sum 2423 89089
# #     t = lt[1]
# #     print(t)
# # # /search_name Иванов
# #     f = open('Phonebook.md','r', encoding='utf-8')
# #     ls = f.read()
# #     ls = ls.replace('# Телефонная книга','')
# #     lst1 = ls.replace('|-----------|-----------|','')
# #     lst2 = lst1.replace('Номер телефона','')
# #     lst3 = lst2.replace('Фамилия Имя Отчество','')
# #     lst4 = lst3.replace('\n','')
# #     lst5 = lst4.split('|')
# #     # print(f' lst5 {lst5}')
# #     # t = input('Введите значение, которое необходимо найти: \n')
# #     for i in range(4, len(lst5)-2, 3):
# #             line = '|' + lst5[i] + '|' + lst5[i+1] + '|'
# #             if t in line:
# #                 await update.message.reply_text(f'{line}\n')
 
    # for i in range(4, len(lst5)):
    #     if t in lst5[i] and lst5[i].isdigit():
    #         await update.message.reply_text(f'{lst5[i-1]} {lst5[i]}') 
    #         # print(f'{lst5[i-1]} {lst5[i]}')
    #     elif t in lst5[i] and not lst5[i].isdigit():
    #         await update.message.reply_text(f'{lst5[i]} {lst5[i + 1]}')
    #     continue
    
    # os.system(search(dt))

 # type: ignore # type: ignore    
# async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     dt = update.message.text
#     print(dt)
#     ls = dt.split() # /sum 2423 89089
#     x = int(ls[1])
#     y = int(ls[2])
#     #  эхо-бот
#     # await update.message.reply_text(f'{dt}') 
#     await update.message.reply_text(f'{x} + {y} = {x + y}') 


# def unknown(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                              text="Sorry, I didn't understand that command.")

#     unknown_handler = MessageHandler(filters.command, unknown)
#     dispatcher.add_handler(unknown_handler)


# async def add_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     os.system("python view_add_hand.py")
#     await update.message.reply_text(f"add")


app = ApplicationBuilder().token("5803182677:AAE7-5Q2HEEQTEibl1KayeA_IXMrEQsokd4").build()


app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("search_name", sum))
# app.add_handler(CommandHandler("add_name", add_name))
# app.add_handler(CommandHandler("look_at_phonebook", look_at_phonebook))



app.run_polling()




# async def look_at_phonebook(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     file = open('Phonebook.md', 'rb')
#     # bot.send_document(chat_id=chat_id, document=open('tests/test.png', 'rb'))
#     look_at_phonebook = InputFile(file)
#     bot.send_document(message.chat_id, file)
#     # os.system("python Phonebook.md")
#     await update.message.reply_text(f"look_at")


#     @dp.message_handler(commands=["photo"])
# async def your_command_handler(message: Message):
#     photo = InputFile(PHOTO_PATH)
#     await message.answer_photo(photo)


# def send_photo_file(chat_id, img):
#     files = {'photo': open(img, 'rb')}
#     requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files)

# async get_file(*, read_timeout=None, write_timeout=None, connect_timeout=None, pool_timeout=None, api_kwargs=None):




# async def send_document(chat_id, document, caption=None, disable_notification=None, reply_to_message_id=None, 
# reply_markup=None, parse_mode=None, thumb=None, disable_content_type_detection=None, allow_sending_without_reply=None, 
# caption_entities=None, protect_content=None, message_thread_id=None, *, filename=None, read_timeout=None, write_timeout=20, 
# connect_timeout=None, pool_timeout=None, api_kwargs=None)
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

# app.add_handler(MessageHandler(filters.Document.FileExtension("py"), msg))

# app.add_handler(MessageHandler(telegram.ext.filters.ALL, msg))
# telegram.ext.filters.ALL
# app.add.handler(MessageHandler(filters.ALL, msg))


# app.add.handler(MessageHandler(filters.ALL, msg))