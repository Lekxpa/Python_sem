# ввод вручную
def symple_add():
    a = []
    fio = input('Введите ФИО:')
    a.append(fio)
    phone_number = input('Введите номер телефона: ')
    a.append(phone_number)
    print(a)
    with open('Phonebook.md', 'a', encoding = 'utf-8') as file:
        file.write(f'\n|{fio}|{phone_number}|')
    file.close()