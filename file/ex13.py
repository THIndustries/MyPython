"""Random name and surname"""
from random import randint

with open('first_names.txt', 'r', encoding='utf-8') as firstname, \
    open('last_names.txt', 'r', encoding='utf-8') as lastname:
    name1 = [i.strip() for i in firstname.readlines()]
    name2 = [i.strip() for i in lastname.readlines()]
    for i in range(3):
        print(name1[randint(0,len(name1))], name2[randint(0,len(name2))])








