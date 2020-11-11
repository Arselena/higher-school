def MadMax(N, Tele):
    try:
        def Max(Mas):
            max = Mas[0]
            ii = 0
            for i in range(len(Mas)):    
                if Mas[i] > max:
                    max = Mas[i]
                    ii = i
            return max, ii

        assert type(N) is int and N > 0 and N % 2 == 1 and N <= 127  # Проверяем число N (целое, положительное, нечетное)
        assert len(Tele) == N  # Проверяем, что длина массива = N
        for i in range(len(Tele)):  
            assert type(Tele[i]) is int and Tele[i] >= 0 and Tele[i] <= 255 # Проверяем Элемент массива (целое, положительное) 
        for i in range(len(Tele)):  # Проверяем, что массив -- неповторяющиеся цифры
            for j in range(i+1, len(Tele)):
                assert Tele[i] != Tele[j]
 
        Impuls = []
        Tele2 = Tele
        for i in range((N + 1) // 2):  # Заполняем правую часть по убыванию
            max, ii = Max(Tele2)
            Impuls.append(max)
            del Tele2[ii]

        for i in range((N - 1) // 2):  # Заполняем левую часть по возрастанию
            max, ii = Max(Tele2)
            Impuls.insert(0,max)
            del Tele2[ii]

        return Impuls
    except AssertionError: 
        pass # Ничего не делать