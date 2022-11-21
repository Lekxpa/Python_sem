# ввод вручную
def symple_add():
    a = []
    fio = input('Введите ФИО:')
    a.append(fio)
    phone_number = input('Введите номер телефона: ')
    a.append(phone_number)
    print(a)
    with open('Phonebook.md', 'a', encoding = 'utf-8') as file:
        file.write(f'|{fio}|{phone_number}|\n')
    # return a
# symple_add()
    
    # def add_csv_txt():
    # ls = symple_add()
    # with open('phonebook.csv', 'a', encoding = 'utf-8') as file:
    #     file.write(f'{ls[0]}; {ls[1]}\n')
    # with open ('phonebook.txt', 'a', encoding = 'utf-8') as filetxt:
    #     filetxt.write(f'ФИО: {ls[0]}  Номер телефона: {ls[1]}')
    # file.close()
    # filetxt.close()