# from tkinter import *

# window = Tk()
# window.title("Телефонный справочник")
# window.mainloop()

# lbl = Label(window, text="Привет")  
# lbl.grid(column=0, row=0)  
# window.mainloop()
# window.geometry("800x600")
# lbl = Label(window, text="Привет", font=("Arial Bold", 20))
 
import tkinter
from tkinter import *
from tkinter import Menu  

def clicked():  
    res = "ФИО" \
            "\n{}".format(txt.get())  
    lbl.configure(text=res)   


def clicked1():  
    res = "Загрузить файл" \
            "\n{}".format(txt.get())  
    lbl.configure(text=res)



# def add_data():

def settings_screen():
    window = Tk()  
    window.title("Телефонный справочник")  
    window.geometry('700x300')
    menu = Menu(window)
    new_item = Menu(menu, fg="blue2", bg="white", tearoff=0)  
    menu.add_cascade(label='Контакты:', menu=new_item)
    new_item.add_command(label='Добавить новый контакт')
    new_item.add_command(label='Посмотреть список контактов')
    window.config(menu=menu)  
# lbl = Label(window, text="Добавить новый контакт:", font=("Arial", 10))  
# lbl.grid(column=0, row=0)
# entry = Entry(fg="yellow", bg="blue", width=50)
# label = Label(text="Имя")
# entry = Entry()
# помещаем кнопку во второй столбец окна, что равно 1. Если вы забудете и поместите кнопку в том же 
# столбце, который равен 0, он покажет только кнопку
    lbl = Label(window, text="ФИО", width = 56, fg="black", bg="cyan", font=("Arial", 10))  
    lbl.grid(column=0, row=1)
# Entry.insert(0, input("Введите ФИО"))
    lbl = Label(window, text="Телефон", width = 30, fg="black", bg="cyan", font=("Arial", 10))  
    lbl.grid(column=1, row=1)
    window.mainloop()

def settings_buttons():
    window = Tk()
    btn1 = Button(window, text="Добавить вручную", bg="cyan", fg="black", command=clicked) 
# изменение цвета кнопки и цвета текста на ней
    btn1.grid(column=0, row=0, ipadx = 10, padx = 5, pady = 5)
    btn2 = Button(window, text="Загрузить файл", bg="cyan", fg="black", command=clicked1) 
# изменение цвета кнопки и цвета текста на ней
    btn2.grid(column=1, row=0, padx = 5, pady = 5)

def user_enter():
# пользовательский ввод
    window = Tk()
    txt = Entry(window,width=75)
    txt.grid(column=0, row=2)
    txt = Entry(window,width=40)
    txt.grid(column=1, row=2) 
    window.mainloop()

def init_view_all():
    window = Tk()
    settings_screen()
    settings_buttons()
    user_enter()
    window.mainloop()


# def screen():
#     lbl = Label(window, text="ФИО", width = 300, fg="black", bg="cyan", font=("Arial", 10))  
#     lbl.grid(column=0, row=1)
#     # Entry.insert(0, input("Введите ФИО"))
#     lbl = Label(window, text="Телефон", width = 50, fg="black", bg="cyan", font=("Arial", 10))  
#     lbl.grid(column=1, row=1)


# def view_data(data):
#     print(f'result = {data}')

# def get_value():
#     return int(input('value =   '))



# background: фоновый цвет

# cursor: курсор указателя мыши при наведении на текстовое поле

# foreground: цвет текста

# font: шрифт текста

# justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю

# show: задает маску для вводимых символов

# state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED

# textvariable: устанавливает привязку к элементу StringVar

# width: ширина элемента

# Элемент Entry имеет ряд методов. Основные из них:

# insert(index, str): вставляет в текстовое поле строку по определенному индексу

# get(): возвращает введенный в текстовое поле текст

# delete(first, last=None): удаляет символ по индексу first. Если указан параметр last, то удаление производится до индекса last. Чтобы удалить до конца, в качестве второго параметра можно использовать значение END.

# focus(): установить фокус на текстовое поле