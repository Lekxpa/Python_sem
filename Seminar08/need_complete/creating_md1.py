def creating_md1():
    with open ('Phonebook.md', 'w', encoding = 'utf-8') as n:
        n.write(f'# Телефонная книга\
    \n|Фамилия Имя Отчество|Номер телефона|Комментарий|\
    \n|-----------|-----------|-----------|\n')
    n.close()