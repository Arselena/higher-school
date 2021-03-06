def MatrixTurn(Matrix:str, M:int, N:int, T:int):

    def rotate(Matrix, i1, i2, j1, j2, Et): # i1, i2, j1, j2 - края 'кольца', Et = Matrix_copy
        if i2+1 // 2 >= len(Matrix) // 2:
            for j in range(j1, j2):
                Matrix[i1][j+1] = Et[i1][j]  # Поворот верхнего края
                Matrix[i2][j] = Et[i2][j+1]  # Поворот нижнего края
            for i in range(i1, i2):
                Matrix[i][j1] = Et[i+1][j1]  # Поворот левого края
                Matrix[i+1][j2] = Et[i][j2]  # Поворот правого края
            rotate(Matrix, i1+1, i2-1, j1+1, j2-1, Et)  # Сужаем кольцо матрицы и снова поворачиваем

    # print('00-', id(Matrix))  # Проверка на совпадение id Matrix в начале

    Matrix_list = list(Matrix)
    for i in range(M):
        Matrix_list[i] = list(Matrix[i])

    Matrix_copy = list(Matrix)  # Создать глубокую копию Matrix
    for i in range(M):
        Matrix_copy[i] = list(Matrix[i])

    rotate(Matrix_list, 0, (M-1), 0, (N-1), Matrix_copy)
    
    for i in range(len(Matrix)):
        Matrix[i] = ''.join(Matrix_list[i])
    
    T -= 1
    if T >= 1:
        MatrixTurn(Matrix, M, N, T)
    # print('01-', id(Matrix)) # Проверка на совпадение id Matrix в конце