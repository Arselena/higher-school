def BigMinus(s1, s2):
    try:
        assert type(s1) is str and type(s2) is str
        assert s1 != '' and s2 != ''

        def modul(x):  # Возвращает модуль x
            if x < 0:
                x = x * (-1)
            return x

        a = int(s1)
        b = int(s2)
        assert 0 <= a <= (10**16) and 0 <= b <= (10**16)

        s = modul(a - b)  # или s = abs(a - b)
        
        return(str(s))

    except AssertionError:
        pass