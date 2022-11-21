def add_txt():
    f = open('phone_add.txt','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('ФИО:', '')
    ls1 = ls.replace('Номер телефона', '')
    ls2 = ls1.replace(':', '|')
    with open('Phonebook.md', 'a', encoding = 'utf-8') as file:
        file.write(f'\n{ls2}')
    f.close()
    file.close()


























    # # print(f'Исходный файл:   {ls}')
    # numbers = ['0','1','2','3','4','5','6','7','8','9']
    # lst = ls.replace('ФИО: ', '')
    # lst1 = lst.replace('  Номер телефона', '')
    # # FIO = []
    # fio = ''
    # for i in range(len(lst1)):
    #     if ":" not in lst1[i]:
    #         # FIO.append(lst1[i])
    #         fio += str(lst1[i])
    #     else:
    #         break
    # phone_number = ''
    # for i in range(len(lst1)):
    #     if '+' in lst1[i] or lst1[i] in numbers:
    #         phone_number += str(lst1[i])

    # with open('Phonebook.md', 'a', encoding = 'utf-8') as file:
    #     file.write(f'|{fio}| {phone_number}|\n')
    # f.close()
    # file.close()

