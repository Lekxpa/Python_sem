from view import symple_add

# def csv_file():
#     with open('phone_dict.csv', 'a', encoding = 'utf-8') as file:
#         file.write(f'ФИО; Номер телефона\n')

def add_csv():
    ls = symple_add()
    with open('phone_dict.csv', 'a', encoding = 'utf-8') as file:
        file.write(f'{ls[0]}; {ls[1]}\n')
