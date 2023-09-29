"""
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
последовательности одинаковых символов заданной строки в подсписки.
"""
result = []
text = input().split()
for i in text:
    if result and i in result[-1]:
        result[-1].append(i)
    else:
        result.append([i])
print(result)