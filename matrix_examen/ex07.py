# Считываем координаты ферзя
move = input()
column = "abcdefgh"
curr = move[0]
col = column.index(curr)
row = 8 - int(move[1])  # Переворачиваем номер строки

# Создаем шахматную доску
board = [["." for _ in range(8)] for _ in range(8)]

# Отмечаем горизонталь и вертикаль
for i in range(8):
    board[row][i] = "*"
    board[i][col] = "*"

# Отмечаем диагонали
for i in range(8):
    for j in range(8):
        if abs(row - i) == abs(col - j):
            board[i][j] = "*"

# Помещаем ферзя
board[row][col] = "Q"

# Выводим доску
for row in board:
    print(" ".join(row))