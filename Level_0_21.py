def BiggerGreater(input:str):

    def perebor(perebor_arr, next):
        perebor_arr_new = []
        N = len(perebor_arr)
        for j in range(N):
            Nj = len(perebor_arr[j])
            for i in range(Nj+1):
                tmp = perebor_arr[j][:]
                if i == Nj:
                    tmp.append(next)
                    perebor_arr_new.append(tmp)
                else:
                    tmp.insert(i, next)
                    perebor_arr_new.append(tmp)
        return perebor_arr_new

    S_str = input
    S_list = list(S_str)
    perebor_arr = []
    perebor_arr.append(S_list[-1:])
    for i in range(len(S_list)-1, 0, -1):
        
        head = (S_str[i-1])  # Голова хвоста
        head_tail = S_str[(i-1):]  # Голова с хвостом

        perebor_arr = perebor(perebor_arr, head)  # Получаем список всех вариантов перебора
        perebor_arr_str = perebor_arr[:]
        for j in range(len(perebor_arr_str)):
            perebor_arr_str[j] = ''.join(perebor_arr_str[j])
        perebor_arr_str.sort()
        
        tail_magic = '-1' 
        for x in range(len(perebor_arr_str)):
            if perebor_arr_str[x] > head_tail:
                tail_magic = perebor_arr_str[x]
                break
        if tail_magic != '-1':
            break
    
    if tail_magic == '-1':
        magic = ''
    else:
        N = len(tail_magic)
        magic = S_str[:-N] + tail_magic

    return magic