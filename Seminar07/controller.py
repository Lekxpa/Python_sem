from creating_md import creating_md
from os.path import exists
from view import select_an_action 

def start():
    path = 'Phonebook.md'
    valid = exists(path)
    if not valid:
        # print(f'not exist')
        creating_md()
        select_an_action()
    else:
        # print(f'exist')
        select_an_action()
start()