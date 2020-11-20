def SumOfThe(N, data):
    try:
        assert type(N) is int and N >= 2 and N == len(data)
        for i in range(len(data)):  
            assert type(data[i]) is int  # Проверяем Элемент массива 

        DATA = list(data)
        SUM = None
        for i in range(1, N):
            if DATA[0] == sum(DATA[1:N]):
                SUM = DATA[0]
                break
            elif DATA[N-1] == sum(DATA[0:(N-1)]):
                SUM = DATA[N-1]
            else: 
                DATA[0], DATA[i] = DATA[i], DATA[0]
        return SUM
    
    except AssertionError:
        pass

print(SumOfThe(7, [100, -50, 10, -25, 90, -35, 90]))