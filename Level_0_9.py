def TheRabbitsFoot(s, encode):
    try:
        assert type(s) is str and s != ''  # Проверяем строку s
        assert type(encode) is bool   # Проверяем слово subs
    
        def delWS(s):  # Удалить пробелы и вернуть строку
            SS = list(s)
            b = s.split()  
            b = "".join(b)
            return b
        
        def StCol(s):   # Подсчет St и Col для Coder
            s = delWS(s) # Извлекаем строку без пробелов
            N = len(s)  # Длина строки
            NN = pow(N, 0.5)  # Кв.корень
            St = int(NN) # Строка и нижняя границв
            Col = int(NN if (NN - int(NN)) == 0 else NN + 1) # Столбец и верхняя граница
            St = St if (St * Col) >= N else (St + 1) # Увеличиваем число строк, если произведение меньше N
            
            if len(s) < (St * Col):  # Добавляем пробелы в последнюю строку, если элементов не хватает
                n = (St * Col) - len(s)
                for i in range(n):
                    s += ' '
            return s, St, Col
 
        def arr(s, St, Col):   # Создаем матрицу NxM (St x Col) для шифровщика
            SS = list(s) 
            ARR = []
            pos = 0
            for i in range(St):
                b = SS[pos:(pos + Col)]
                ARR.append(b)
                pos += Col
            return ARR
        
        def arr2(s):  # Создаем матрицу для дешифровщика
            SS = list(s)
            ARR = []
            pos = 0
            j = 0
            for i in range(len(SS)):
                if SS[i] == ' ' or (i == len(SS) - 1) :
                    if SS[i] == ' ':
                        b = SS[pos:i]
                    else:
                        b = SS[pos:(i + 1)]
                    ARR.append(b)
                    pos += len(b) + 1
                    assert len(ARR[j]) == len(ARR[0]) or len(ARR[j]) + 1 == len(ARR[0])   
                    if len(ARR[j]) != len(ARR[0]):
                        ARR[j].append(' ')
                    j += 1
            St = len(ARR)
            Col = len(ARR[0])
            return ARR, St, Col

        def Shifr(s, St, Col): # Транспортируем матрицу
            arrTrans = []
            for j in range(Col):
                tmp2 = []
                for i in range(St):
                    tmp2.append(s[i][j])
                arrTrans.append(tmp2)
            return arrTrans

        def Coder(s):
            s, St, Col = StCol(s)
            s = arr(s, St, Col)
            arrTrans = Shifr(s, St, Col)
            shifr = []
            for i in range(len(arrTrans)): # Формируем шифр - строку с пробелами
                j = len(arrTrans[i])
                if arrTrans[i][j-1] != ' ':
                    arrTrans[i].append(' ')
                shifr += arrTrans[i]
            SHIFR = "".join(shifr)
            return SHIFR

        def deCoder(s):
            s, St, Col = arr2(s)
            arrTrans = Shifr(s, St, Col)
            shifr = []
            for i in range(len(arrTrans)): 
                shifr += arrTrans[i]
            SHIFR = delWS("".join(shifr))
            return SHIFR

        if encode == True:
            return(Coder(s))
        else:
            assert "  " not in s  # Проверяем, что в строке не более 1 пробела
            return(deCoder(s))
    
    except AssertionError:
        pass