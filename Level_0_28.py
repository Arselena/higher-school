def Keymaker(k:int):
    def open_close(S, n):
        for i in range(n-1, len(S), n): # меняем положение дверей от n-1 с шагом n
            if S[i] == 1:
                S[i] = 0
            else:
                S[i] = 1
        return S

    S = [0] * k # массив закрытых дверей
    for i in range(1, k+1):
        if i == 1:
            S = list(map(lambda x: x+1, S))  # 1-ая итерация, открываем все двери
        else:
            S = open_close(S, i)
    
    S = list(map(str, S))
    S = ''.join(S)
    
    return S