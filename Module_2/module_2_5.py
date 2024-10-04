def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
value = input('Введите значения матрицы: ')
matrix = get_matrix(n, m, value)

if n <= 0:
    print('Задано неверное количество строк:', n)
elif m <=0:
    print('Задано неверное количество столбцов:' ,m)
else:
    for i in matrix:
         print(*i)