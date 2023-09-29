# Ввод строки и создание списка
text = input().split()
# Инициализация списка подсписков
sublists = []
sublists.append([])
# Генерация подсписков
for i in range(len(text) + 1):
    for j in range(i + 1, len(text) + 1):
        sublist = text[i:j]
        sublists.append(sublist)

# Вывод подсписков
print(sorted(sublists, key=len))
