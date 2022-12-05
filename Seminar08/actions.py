from creating_md import creating_md

def show_phonbook_terminal():
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('# ','\n\t')
    lst1 = ls.replace('|-----------|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('Комментарий','')
    lst4=lst4.replace('|','       ')
    print(f'{lst4}\n')


def search():
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('# Телефонная книга','')
    lst1 = ls.replace('|-----------|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('Комментарий','')
    lst4 = lst4.replace('\n','')
    lst5 = lst4.split('|')
    # print(f' lst5 {lst5}')
    t = input('Введите значение, которое необходимо найти: \n')
    for i in range(5, len(lst5)-2, 4):
        # line = '|' + lst5[i] + '|' + lst5[i+1] + '|' + lst5[i+2] + '|'
        line = lst5[i] + '  ' + lst5[i+1] + '  ' + lst5[i+2]
        if t in line:
            print(line)


def del_dt():
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

    t = input('Введите значение, которое необходимо удалить: \n')
    line = 0
    with open ('Phonebook.md', 'a', encoding = 'utf-8') as filedel:
        creating_md()
        for i in range(5, len(lst5)-2, 4):
            line = '|' + lst5[i] + '|' + lst5[i+1] + '|' + lst5[i+2] + '|'
            if t not in line:
                filedel.write(f'{line}\n')