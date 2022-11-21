def csv_file():
    v = open('phone_add.csv','r', encoding='utf-8')
    ls = v.read()
    ls = ls.replace(';', '|')
    with open('Phonebook.md', 'a', encoding = 'utf-8') as filecsv:
        filecsv.write(f'\n|{ls}|\n|')
    v.close()
    filecsv.close()













#     # ls = v.read().splitlines()
#     fio = ''
#     for i in range(len(ls)):
#         # for j in i:
#         if ";" not in ls[i]:
#             # FIO.append(ls[i])
#             # tuple(elem_str.split(';')) for elem_str in ls
#             fio += str(ls[i])
#             ls.replace('ls[i]', '')
#         else:
#             ls.replace('ls[i]', '')
#             # continue
#     with open('Phonebook.md', 'a', encoding = 'utf-8') as filecsv:
#         filecsv.write(f'|{fio}|')
            # break
        # ls.rstrip(fio)
        # continue
    # print(fio)
    # phone = []
    # numbers = ['0','1','2','3','4','5','6','7','8','9']
    # phone_number = ''
    # for i in range(len(ls)):
    #     if '+' in ls[i] or ls[i] in numbers and ';' not in ls[i]:
    #         # phone.append(ls[i])
    #         phone_number += str(ls[i])
    #     else:
    #         break
    #     # ls.rstrip(phone_number)
    #     # continue
    # print(phone_number)

    # with open('Phonebook.md', 'a', encoding = 'utf-8') as filecsv:
    #     filecsv.write(f'\n|{fio}|{phone_number}|\n')
    # v.close()
    # filecsv.close()

# phone = []
# numbers = ['0','1','2','3','4','5','6','7','8','9']
# phone_number = ''
# for i in range(len(lst1)):
#     if '+' in lst1[i] or lst1[i] in numbers:
#         phone.append(lst1[i])
#         phone_number += str(lst1[i])
# print(phone_number)

# lst2 = lst1.replace(phone_number, '')
# print(lst2)