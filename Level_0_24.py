def MatrixTurn(Matrix:str, M:int, N:int, T:int):

    Matrix = list(Matrix)
    for i in range(M):
        Matrix[i] = list(Matrix[i])

    Matrix_copy = list(Matrix)  # Создать глубокую копию Matrix
    for i in range(M):
        Matrix_copy[i] = list(Matrix[i])

    i1 = 0
    i2 = M-1
    j1 = 0
    j2 = N-1
    while i2+1 // 2 >= len(Matrix) // 2:
        for j in range(j1, j2):
            Matrix[i1][j+1] = Matrix_copy[i1][j]  # Поворот верхнего края
            Matrix[i2][j] = Matrix_copy[i2][j+1]  # Поворот нижнего края
        for i in range(i1, i2):
            Matrix[i][j1] = Matrix_copy[i+1][j1]  # Поворот левого края
            Matrix[i+1][j2] = Matrix_copy[i][j2]  # Поворот правого края
        i1 += 1
        i2 -= 1
        j1 += 1
        j2 -= 1
    
    for i in range(len(Matrix)):
        Matrix[i] = ''.join(Matrix[i])
    
    T -= 1
    if T >= 1:
        MatrixTurn(Matrix, M, N, T)