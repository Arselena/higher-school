def squirrel(N):
    try:
        if type(N) is int:  # Проверяем целое ли число N
            assert N >= 0, 'задайте целое число N >= 0'   
            if N == 0:  # Возвращаем 0!=1
                return 1
            else:  # Вычичляем факториал
                F = 1
                for i in range(1, N+1):
                    F *= i
                if F < 10:   # Возвращаем факториал, если факториал < 10
                    return F
                else:
                    while F > 10:  # Ищем первую цифру, если факториал > 10
                        F //= 10
                    return F
    except AssertionError:  # Ловим исключение N < 0
        Val = False
    except TypeError:  # Ловим исключение не верного типа
        Val = False
