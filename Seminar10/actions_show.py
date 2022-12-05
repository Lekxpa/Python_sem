def show_phonbook_terminal():
    f = open('Phonebook.md','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('# ','\n\t')
    lst1 = ls.replace('|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    lst4 = lst3.replace('|','\t')
    print(f'{lst4}\n')