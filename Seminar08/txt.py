def add_txt():
    f = open('phone_add.txt','r', encoding='utf-8')
    ls = f.read()
    ls = ls.replace('ФИО','')
    ls1 = ls.replace(' Номер телефона','')
    ls11 = ls1.replace(' Комментарий','')
    ls11 = ls11.replace('\n','')
    ls2 = ls11.split(':')
    with open('Phonebook.md', 'a', encoding = 'utf-8') as file:
        for i in range(1,len(ls2),3):
            file.write(f'|{ls2[i]}|{ls2[i+1]}|{ls2[i+2]}|\n')
    f.close()
    file.close()