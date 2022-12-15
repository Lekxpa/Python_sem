from creating_md1 import creating_md1
def show_phonbook_terminal():
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('# ','\n\t')
    lst1 = ls.replace('|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('|','\t')
    print(f'{lst4}\n')


def search():
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('# Телефонная книга','')
    lst1 = ls.replace('|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('\n','')
    lst5 = lst4.split('|')
    # print(f' lst5 {lst5}')
    t =  update.message.text
    # t = input('Введите значение, которое необходимо найти: \n')
    for i in range(4, len(lst5)):
        if t in lst5[i] and lst5[i].isdigit():
            print(f'{lst5[i-1]} {lst5[i]}')
        elif t in lst5[i] and not lst5[i].isdigit():
            print(f'{lst5[i]} {lst5[i + 1]}')
        continue



def del_dt():
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    print(f'{ls}')
    ls = ls.replace('# Телефонная книга','')
    lst1 = ls.replace('|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('\n','')
    lst5 = lst4.split('|')

    t = input('Введите значение, которое необходимо удалить: \n')
    line = 0
    with open ('Phonebook.md', 'a', encoding = 'utf-8') as filedel:
        creating_md1()
        for i in range(4, len(lst5)-2, 3):
            line = '|' + lst5[i] + '|' + lst5[i+1] + '|'
            if t not in line:
                filedel.write(f'{line}\n')