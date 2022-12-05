# import json
# import contriller
# path_to_db = 'db.json'

# def json_file():
#     v = open('Phonebook.md','r', encoding='utf-8')
#     ls = v.read()
#     lst = ls.replace('# Телефонная книга','')
#     lst1 = lst.replace('|-----------|-----------|','')
#     lst2 = lst1.replace('Номер телефона','')
#     lst3 = lst2.replace('Фамилия Имя Отчество','')
#     ls4 = lst3.replace('\n','')
#     lst_end = ls4.split('|')
#     with open ('phonebook1.txt', 'w', encoding = 'utf-8') as file_json:
#         dt = json.load(file_json)
#         for i in range(4,len(lst_end),3):
           
#             file_json.write(f'{lst_end[i]};{lst_end[i+1]};\n')
            
# '\n' + "".join(data[i]['Name']) + ' ' + "".join(
#                         data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

#     v.close()
#     file_json.close()

# def export_txt():
#     # name = input('Введите имя или фамилию контакта, для экспорта в файл:  ')

#     with open(path_to_db, 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#         for i in range(0, len(data)):
#            # if name == data[i]['Name'] or name == data[i]['Surname']:
#                 with open('Export_contact.txt', 'a') as export:
#                     export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
#                         data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))