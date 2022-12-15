from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import creating_md

# t.me/Test_gb_lekbot

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!\n\
        \nОбщежитие слушает! :)\n\
        \nДля работы с Телефонной книгой напишите /menu и отправьте сообщение!')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/hello\n/all_phonebook\n/search\n/add\n/delete\n/bye")

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
    for i in range(5, len(lst5)-2, 4):
        line = lst5[i] + '  ' + lst5[i+1] + '  ' + lst5[i+2]
        if a in line:
            await update.message.reply_text(f'{line}')

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t =  update.message.text
    print(t)
    t1 = t.replace("/add ", "")
    t2 = t1.split(",")
    print(t2[0])
    print(t2[1])
    print(t2[2])
    with open('Phonebook.md', 'a', encoding = 'utf-8') as file:
        file.write(f'|{t2[0]}|{t2[1]}|{t2[2]}|\n')
        print(file)


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
    await update.message.reply_text(f" See you, {update.effective_user.first_name}!")

app = ApplicationBuilder().token("5803182677:AAE7-5Q2HEEQTEibl1KayeA_IXMrEQsokd4").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("all_phonebook", all_phonebook))
app.add_handler(CommandHandler("search", search))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("delete", delete))
app.add_handler(CommandHandler("bye", bye))

app.run_polling()

# t.me/Test_gb_lekbot