def MatrixTurn(Matrix:str, M:int, N:int, T:int):

    def rotate(S, i1, i2, j1, j2, Et): # i1, i2, j1, j2 - края 'кольца', Et - эталонная(первоначальная) матрица
        if i2+1 // 2 >= len(S) // 2:
            for j in range(j1, j2):
                S[i1][j+1] = Et[i1][j]  # Поворот верхнего края
                S[i2][j] = Et[i2][j+1]  # Поворот нижнего края
            for i in range(i1, i2):
                S[i][j1] = Et[i+1][j1]  # Поворот левого края
                S[i+1][j2] = Et[i][j2]  # Поворот правого края
            rotate(S, i1+1, i2-1, j1+1, j2-1, Et)  # Сужаем кольцо матрицы и снова поворачиваем
        # else:  Думяю, это лишние строки
            # return S
        return S

    if T >= 1:
        S = list(Matrix)  # Создать глубокую копию Matrix
        for i in range(M):
            S[i] = list(Matrix[i])
        
        Matrix = rotate(S, 0, (len(S)-1), 0, (len(S[0])-1), Matrix)
        T -= 1
        for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                Matrix[i] = ''.join(Matrix[i])
        
        Matrix = MatrixTurn(S, M, N, T)