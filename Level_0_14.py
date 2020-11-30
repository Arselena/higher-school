def Unmanned(L, N, track):  # L - длина дороги
                            # N - кол-во светофоров
                            # track - момент вр. от начала дороги, вр. показа красного света и время показа зелёного цвета
    try:    
        def light(t, r, g):
            k = t % (r + g)
            ost = r - t % (r + g)  # сколько осталсь гореть красному сигналу светофора
            if (0 < ost <= r):
                pos = 'red' 
            else:
                pos = 'green'  
            
            return pos, ost

        assert type(L) is int and L > 0
        assert type(N) is int and N > 0
        for i in range(len(track)):
            assert N == len(track)
            if i < (N - 1):
                assert track[i + 1][0] >= track[i][0] # послед.момент времени от нач.дорогт больше предыдущего
            for j in range(len(track[i])):
                assert type(track[i][j]) is int

        t = 0  # время ожидания на светофорах
        for i in range(N):  # цикл по светофорам
            pos, ost = light((track[i][0] + t), track[i][1], track[i][2])
            if L > track[i][0] and pos == 'red':
                t += ost
        T = L + t  # время в пути 

        return T

    except AssertionError:
        pass