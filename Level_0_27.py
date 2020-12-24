def Football(F, N:int):
    F = list(F)
    F_sort = sorted(F)
    F_rev = reversed(F)    
    index = []

    if F == F_sort:  # Если массив изначально отсортирован
        return False
    
    for i in range(len(F)):  # Запишем индексы значений не на своих местах
        if F[i] != F_sort[i]:
            index.append(i)

    if len(index) == 2:  # если не совпали два значения
        return True
    elif index not in list(range(index[0], (index[0] + len(index) + 1))): # если не совпадения идут не по порядку
        return False
    
    for i in index:  # усли размернутый массив совпадает с отсортированным в диапазоне индексов не на своем месте
        if F_rev[index[i]] != F_sort[index[i]]:
            return False
    return True