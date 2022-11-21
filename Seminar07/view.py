import csv_add
import txt_save
import txt
# import view_add_hand
from view_add_hand import symple_add
import csv_save

# выбор действия - загрузка или выгрузка данных
def select_an_action():
    data = int(input('Выберите действие: \
        \n1. Добавить данные в справочник\
        \n2. Выгрузить данные из справочника\n'))
    if data == 1:
        dt = int(input('Выберите порядок ввода данных: \
            \n1. Добавить данные вручную\
            \n2. Добавить данные из файла\n'))
        if dt == 1:
            symple_add()
        elif dt == 2:
            version = int(input('Выберите формат загружаемого файла:\n\
                    \n1. загрузить файл в формате csv\
                    \n2. загрузить файл в формате txt\n'))
            if version == 1:
                csv_add.csv_file()
            elif version == 2:
                txt.add_txt()
            else:
                print('Неверно выбрано действие. Попробуйте еще раз!')
        else:
            print('Неверно выбрано действие. Попробуйте еще раз!')
        # return dt
    elif data == 2:
        variant = int(input('Выберите формат выгрузки данных:\n\
                    \n1. выгрузить файл в формате csv\n\
                    \n2. выгрузить файл в формате txt\n'))
        if variant == 1:
            csv_save.csv_file()
        elif variant == 2:
            txt_save.txt_file()
        else:
            print('Неверно выбрано действие. Попробуйте еще раз!')
    else:
        print('Неверно выбрано действие. Попробуйте еще раз!')
    # return data
    # break
select_an_action()

# # # ввод вручную
# def symple_add():
#     a = []
#     fio = input('Введите ФИО:')
#     a.append(fio)
#     phone_number = input('Введите номер телефона: ')
#     a.append(phone_number)
#     print(a)
#     return a


# #  загрузка данных из файла
# def gen_dict():
#     version = int(input('Выберите формат загружаемого файла:\n\
#         \n1. загрузить файл в формате csv\n\
#         \n2. загрузить файл в формате txt\n'))
#     if version == 1:
#         csv_add.csv_file()
#     elif version == 2:
#         txt.add_txt()
#     else:
#         print('Неверно выбрано действие. Попробуйте еще раз!')
#     # return version
# gen_dict()