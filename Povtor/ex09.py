"""
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
Для этого они решили сыграть в камень, ножницы и бумагу.
Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.
"""

# Ввод выборов Тимура и Руслана
timur_choice = input()
ruslan_choice = input()

# Проверяем условия и определяем победителя
if timur_choice == ruslan_choice:
    print("Ничья")
elif (timur_choice == "камень" and ruslan_choice == "ножницы") or \
     (timur_choice == "ножницы" and ruslan_choice == "бумага") or \
     (timur_choice == "бумага" and ruslan_choice == "камень"):
    print("Тимур")
else:
    print("Руслан")



