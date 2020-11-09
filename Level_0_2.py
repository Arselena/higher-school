def odometer(oksana):
    try:
        assert len(oksana) >= 2 # Проверяем, что длина массива >=2

        # Если длина массива нечетна, то уменьшаем ее на 1. Т.е. считаем, что с последней скоростью мотоциклист не перемещался
        if len(oksana) % 2 == 0:
            N = len(oksana)
        else:
            N = len(oksana) - 1
        
        S = 0  # Расстояние
        t1 = 0  # Предыдущее время с начала поездки
        for i in range(1, N, 2):
            assert type(oksana[i]) is int and type(oksana[0] ) is int # Проверяем целое ли число в массиве
            assert oksana[i] >= 0 and oksana[0] >= 0 # Проверяем положительное ли число в массиве
            assert (oksana[i] - t1) > 0 # Проверяем, что пред.время меньше текущего
            
            S += (oksana[i-1]) * (oksana[i] - t1) # скорость * время поездки с этой скоростью
            t1 = oksana[i] # Запоминаем пред.время
        return S
    except AssertionError: 
        pass # Ничего не делать