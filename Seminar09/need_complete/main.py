import controller

data = input('Выберите действие: \
    \n1. Добавить данные в справочник\
    \n2. Выгрузить данные из справочника\n')
if data == 1:
    controller.choise_format_add()
elif data == 2:
    controller.gen_dict()
else:
    print('Неверно выбрано действие. Попробуйте еще раз!')









# import controller as c
# c.button_click()
# c.button_click1()
