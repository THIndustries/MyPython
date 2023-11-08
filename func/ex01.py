def matrix(n=1, m=None, value=0):
    my2dlist = []
    if m is None:
        m = n
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(value)
        my2dlist.append(temp)
    return my2dlist


print(matrix())  # матрица 1 × 1 из 0
print(matrix(3))  # матрица 3 × 3 из 0
print(matrix(2, 5))  # матрица 2 × 5 из 0
print(matrix(3, 4, 9))
