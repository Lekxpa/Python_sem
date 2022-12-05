def csv_file():   
    v = open('phone_add.csv','r', encoding='utf-8')
    lst_str = v.read()
    lst_str11 = lst_str.replace('\n','')
    lst_str1 = lst_str11.split(';')
    with open('Phonebook.md', 'a', encoding = 'utf-8') as filecsv:
        for i in range(0,len(lst_str1)-1,2):
            filecsv.write(f'\n|{lst_str1[i]}|{lst_str1[i+1]}|')
    v.close()
    filecsv.close()