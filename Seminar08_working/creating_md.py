def creating_md():
    with open ('Phonebook.md', 'w', encoding = 'utf-8') as n:
        n.write(f'# Телефонная книга\
    \n|Фамилия Имя Отчество|Номер телефона|\
    \n|-----------|-----------|')
    n.close()