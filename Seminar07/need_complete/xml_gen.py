from model import symple_add
from model import contrary_add
from model import file_csv
from model import file_xml

def create(fio, phone_number):
    xml = '<xml>\n'
    xml += ' <ФИО = {}</ФИО>\n'\
        .format(symple_add(fio))
    xml += ' <Номер телефона = >{}</Номер телефона>\n'\
        .format(symple_add(phone_number))
    xml += '</xml>'

    with open('phone_dict.xml', 'a') as filex:
        filex.write('{};' '{}\n'
                    .format(fio, phone_number))

    # with open('data.xml', 'w') as page:
    #     page.write(xml)
    # return xml

