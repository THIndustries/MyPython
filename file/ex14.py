"""Необычные страны"""
with open('population.txt', 'r', encoding='utf-8') as file:
    text = list(filter(lambda x: x[0][0] == 'G' and int(x[1]) > 500_000,[i.strip().split('\t') for i in file.readlines()]))
    for i in text:
        print(i[0])






