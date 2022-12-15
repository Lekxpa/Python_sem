from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import creating_md


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}\n\
        \nобщежитие слушает! :)\n\
        \nДля работы с Телефонной книгой напишите /menu и отправьте сообщение!')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/hello\n/all_phonebook\n/search\n/delete\n/bye")

async def all_phonebook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('# ','\n\t')
    lst1 = ls.replace('|-----------|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('Комментарий','')
    lst4=lst4.replace('|','       ')
    print(f'{lst4}\n')
    await update.message.reply_text(f'{lst4}\n')


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('# Телефонная книга','')
    lst1 = ls.replace('|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('\n','')
    lst5 = lst4.split('|')
    t =  update.message.text
    print(t)
    t1 = t.split(" ")
    a = t1[1]
    for i in range(4, len(lst5)):
        if a in lst5[i] and lst5[i].isdigit():
            await update.message.reply_text(f'{lst5[i-1]} {lst5[i]}')
        elif a in lst5[i] and not lst5[i].isdigit():
            await update.message.reply_text(f'{lst5[i]} {lst5[i + 1]}')
        

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    print(f'{ls}')
    ls = ls.replace('# Телефонная книга','')
    lst1 = ls.replace('|-----------|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('Комментарий','')
    lst4 = lst4.replace('\n','')
    lst5 = lst4.split('|')
    t =  update.message.text
    print(t)
    t1 = t.split(" ")
    a = t1[1]
    line = 0
    with open ('Phonebook.md', 'a', encoding = 'utf-8') as filedel:
        creating_md.creating_md()
        for i in range(5, len(lst5)-2, 4):
            line = '|' + lst5[i] + '|' + lst5[i+1] + '|' + lst5[i+2] + '|'
            if a not in line:
                filedel.write(f'{line}\n')


async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f" See you, {update.effective_user.first_name}")

app = ApplicationBuilder().token("5803182677:AAE7-5Q2HEEQTEibl1KayeA_IXMrEQsokd4").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("all_phonebook", all_phonebook))
app.add_handler(CommandHandler("search", search))
app.add_handler(CommandHandler("delete", delete))
app.add_handler(CommandHandler("bye", bye))

app.run_polling()

# t.me/Test_gb_lekbot