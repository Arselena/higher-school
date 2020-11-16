def PatternUnlock(N, hits):
    try:
        assert type(N) is int and N > 0 # Проверяем число N (целое, положительное)
        assert N == len(hits)
        for i in range(len(hits)):  
            assert type(hits[i]) is int and  1 <= hits[i] <= 9 # Проверяем Элемент массива (целое, положительное) 
        
        def length(pos, next):
            leng = 0
            if (pos == 1 and next in (6, 2, 9) or
            pos == 2 and next in (1, 3, 5, 8) or 
            pos == 3 and next in (2, 4, 7) or 
            pos == 4 and next in (3, 5) or
            pos == 5 and next in (2, 4, 6) or
            pos == 6 and next in (1, 5) or
            pos == 7 and next in (3, 8) or
            pos == 8 and next in (2, 7, 9) or
            pos == 9 and next in (1, 8)):
                leng = 1
            
            elif (pos == 1 and next in (5, 8) or
                pos == 2 and next in (4, 6, 7, 9) or 
                pos == 3 and next in (5, 8) or
                pos == 4 and next == 2 or
                pos == 5 and next in (3, 1) or
                pos == 6 and next == 2 or 
                pos == 7 and next == 2 or
                pos == 8 and next in (1, 3) or 
                pos == 9 and next == 2):
                leng = pow(2, 0.5)
            return leng        
            
        # Считаем сумму, 
        sum = 0
        for i in range(N-1):
            sum += length(hits[i], hits[i+1])
        a = list(str(round(sum * pow(10, 5)))) # Округляем и переводим в строку
        
        # Удаляем 0 и преобразуем в строку
        b = []
        i = 0
        while i < len(a):
            if a[i] != '0':
                b.append(a[i])
            i += 1
        S = "".join(b)

        return S
    
    except AssertionError:
        pass

SS = PatternUnlock(0, [])
# SS = PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9])    
print(SS)
#print(type(SS))