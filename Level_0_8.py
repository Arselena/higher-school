def SumOfThe(N, data):
    try:
        assert type(N) is int and N >= 2 and N == len(data)
        for i in range(len(data)):  
            assert type(data[i]) is int  # Проверяем Элемент массива 

        DATA = list(data)
        for i in range(1, N):
            if DATA[0] == sum(DATA[1:(len(DATA))]):
                SUM = DATA[0]
                break
            elif i == N-1:
                SUM = None
            else: 
                DATA[0], DATA[i] = DATA[i], DATA[0]
        return SUM
    
    except AssertionError:
        pass

print(SumOfThe(7, (100, -50, 10, -25, 90, -35, 90)))