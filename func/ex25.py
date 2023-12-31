"""Напишите функцию func, используя синтаксис анонимных функций,
которая принимает строковый аргумент и возвращает значение True,
если переданный аргумент начинается и заканчивается на английскую букву
a (регистр буквы неважен) и False в противном случае."""

func = lambda x: x[0].lower() == x[-1].lower() and (x[0] in 'Aa' and x[-1] in 'Aa')

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
print(func('bfrefrB'))



