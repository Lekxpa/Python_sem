def txt_file():
    m = open('Phonebook.md','r', encoding='utf-8')
    ls = m.read()
    lst = ls.replace('# Телефонная книга','')
    lst1 = lst.replace('|-----------|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    ls4 = lst3.replace('Комментарий','')
    ls4 = ls4.replace('\n','')
    lst_end = ls4.split('|')
    with open ('phonebook.txt', 'w', encoding = 'utf-8') as filetxt:
        for i in range(5,len(lst_end),4):
            filetxt.write(f'ФИО:{lst_end[i]} Номер телефона:{lst_end[i+1]} Комментарий:{lst_end[i+2]}\n')
    m.close()
    filetxt.close()