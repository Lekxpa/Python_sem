def txt_file():
    m = open('Phonebook.md','r', encoding='utf-8')
    ls = m.read()
    # print(f'Исходный файл:   {ls}')
    lst = ls.replace('Телефонная книга', '')
    lst1 = lst.replace('Номер телефона', '')
    lst2 = lst1.replace('Фамилия Имя Отчество', '')
    lst3 = lst2.replace('|', ':')

    with open('phonebook.txt', 'a', encoding = 'utf-8') as filetxt:
        filetxt.write(f'ФИО: {lst3} Номер телефона: {lst3}')
    m.close()
    filetxt.close()

    # # print(lst2)
    # # FIO = []
    # fio = ''
    # for i in range(1,len(lst2)):
    #     if "|" not in lst2[i]:
    #         # FIO.append(lst2[i])
    #         fio += str(lst2[i])
    #     else:
    #         break
    # # print(fio)
    # # phone = []
    # numbers = ['0','1','2','3','4','5','6','7','8','9']
    # phone_number = ''
    # for i in range(1,len(lst2)):
    #     if '+' in lst2[i] or lst2[i] in numbers:
    #         # phone.append(lst2[i])
    #         phone_number += str(lst2[i])
    # print(phone_number)

    # with open('phonebook.txt', 'a', encoding = 'utf-8') as filetxt:
    #     filetxt.write(f'ФИО: {fio}  Номер телефона: {phone_number}\n')
    # m.close()
    # filetxt.close()