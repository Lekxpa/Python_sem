# from view_add_hand import symple_add
# import view_add_hand

# def csv_file():
#     with open('phone_dict.csv', 'a', encoding = 'utf-8') as file:
#         file.write(f'Фамилия;Номер телефона\n')

# def add_csv_txt():
#     ls = symple_add()
#     with open('phonebook.csv', 'a', encoding = 'utf-8') as file:
#         file.write(f'{ls[0]}; {ls[1]}\n')
#     with open ('phonebook.txt', 'a', encoding = 'utf-8') as filetxt:
#         filetxt.write(f'ФИО: {ls[0]}  Номер телефона: {ls[1]}')
#     file.close()
#     filetxt.close()

def csv_file():
    v = open('Phonebook.md','r', encoding='utf-8')
    ls = v.read()
    # print(f'Исходный файл:   {ls}')
    lst = ls.replace('Телефонная книга', '')
    lst11 = lst.replace('-','')
    lst1 = lst11.replace('Номер телефона', '')
    lst2 = lst1.replace('Фамилия Имя Отчество', '')
    lst3 = lst2.replace('|', ';')

    with open('phonebook.csv', 'a', encoding = 'utf-8') as filecsv:
        filecsv.write(f'\n{lst3}')
    v.close()
    filecsv.close()






    # print(lst2)
    # FIO = []
    # fio = ''
    # for i in range(1,len(lst2)):
    #     if "|" not in lst2[i]:
    #         FIO.append(lst2[i])
    #         fio += str(lst2[i])
    #     # else:
    #     #     break
    #     continue
    # # print(fio)
    # phone = []
    # numbers = ['0','1','2','3','4','5','6','7','8','9']
    # phone_number = ''
    # for i in range(1,len(lst2)):
    #     if '+' in lst2[i] or lst2[i] in numbers:
    #         phone.append(lst2[i])
    #         phone_number += str(lst2[i])
    #     else:
    #         break
    # print(phone_number)

    # with open('phonebook.csv', 'a', encoding = 'utf-8') as filecsv:
    #     filecsv.write(f'{fio}, {phone_number}\n')
    # v.close()
    # filecsv.close()