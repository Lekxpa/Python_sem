# from random import randint

import string
import re

# def get_fio:
    

# def get_numberphone:
    
def symple_add():
    fio = input('Введите ФИО:')
    phone_number = input('Введите номер телефона: ')

def contrary_add():
    phone_number = input('Введите номер телефона: ')
    fio = input('Введите ФИО:')

def file_csv():
    f = open('TelDict.csv','r', encoding='utf-8')
    ls = f.read()
    print(f'{ls}')


def file_xml():
    p = open('TelDict.csv','r', encoding='utf-8')
    xml_f = p.read()
    print(f'{xml_f}')