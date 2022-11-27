def csv_file():
    v = open('Phonebook.md','r', encoding='utf-8')
    ls = v.read()
    lst = ls.replace('# Телефонная книга','')
    lst1 = lst.replace('|-----------|-----------|','')
    lst2 = lst1.replace('Номер телефона','')
    lst3 = lst2.replace('Фамилия Имя Отчество','')
    ls4 = lst3.replace('\n','')
    lst_end = ls4.split('|')
    with open ('phonebook.csv', 'a', encoding = 'utf-8') as filecsv:
        for i in range(4,len(lst_end),3):
            filecsv.write(f'{lst_end[i]};{lst_end[i+1]};\n')
    v.close()
    filecsv.close()