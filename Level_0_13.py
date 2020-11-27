def UFO(N, data, octal):
    try:    
        def trans(num, SS):
            arr = list(int(d) for d in str(num))
            n = len(arr)
            sum = 0
            for i in range(n):
                if SS == 8:
                    assert arr[i] < 8  # исключаем цифры 8 и 9 в восьмеричной CC
                sum += arr[i] * (SS ** (n - 1))
                n -= 1
            return sum
        
        assert type(N) is int and N == len(data)
        assert type(octal) is bool
        for d in data:
            assert type(d) is int

        if octal == True:
            SS = 8
        else:
            SS = 16 
        
        ARR = []
        for d in data:
            ARR.append(trans(d, SS))
        
        return ARR
    
    except AssertionError:
        pass