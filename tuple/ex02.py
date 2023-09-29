# Ввод коэффициентов a, b, c
a = int(input())
b = int(input())
c = int(input())

# Вычисление координат вершины параболы
x_vertex = -b / (2 * a)
y_vertex = 4 * a * c - b**2 / (4 * a)

# Вывод координат вершины
print(f'({x_vertex}; {y_vertex})')
