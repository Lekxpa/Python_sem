# ввод вручную
def symple_add():
    a = []
    fio = input('Введите ФИО:')
    a.append(fio)
    phone_number = input('Введите номер телефона: ')
    a.append(phone_number)
    comment = input('Введите комментарий: ')
    a.append(comment)
    print(a)
    with open('Phonebook.md', 'a', encoding = 'utf-8') as file:
        file.write(f'|{fio}|{phone_number}|{comment}|\n')
    file.close()