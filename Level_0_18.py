def MisterRobot(N:int, data:int):
    def min(n, s):  # Находим min из элементов, которые стоят не на своих местах
        index = 0
        min = n
        for i, val in enumerate(s):
            if val != (i + 1) and val < min:
                min = val
                index = i
        return index

    def shift_left(index, s):
        i = s[index] - 1
        pos = 0
        while index != i or pos > 100:
            if index == len(s) - 1:
                a1, a2, a3 = (index - 2), (index - 1), (index)
                s[a1], s[a2], s[a3] = s[a2], s[a3], s[a1]
            else:
                a1, a2, a3 = (index - 1), index, (index + 1)
                s[a1], s[a2], s[a3] = s[a2], s[a3], s[a1]
            index -= 1
            pos += 1
        return s
    
    data_new = data
    index = N - 1
    pos = 0
    while index != 0 or pos == 100: # Пока есть min не на своем месте
        index = min(N, data_new)
        if index == (N - 1) and data_new[index] == data_new[index - 1] - 1:
            return False
        else:
            data_new = shift_left(index, data_new)
        pos += 1
    if pos == 100:
        return "ой"
    else:
        return True