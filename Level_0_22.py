def SherlockValidString(s:str):
    s_list = list(s)
    unique = set(s_list)  # Уникальные элементы в строке
    count_list = []
    for i in unique:  # Кол-во уникальных элементов
        n = s_list.count(i)
        count_list.append(n)
    count_list.sort()
    unique2 = list(set(count_list))  # Уникальные кол-ва встречаемых элементов

    if len(unique2) == 1:  # если все эл-ы встречаются по 1 разу
        return True
    elif len(unique2) == 2 and count_list.count(1) == 1: # один отличается от остальных и кол-во этого одного = 1
        return True
    elif len(unique2) == 2 and count_list.count(count_list[-1]) == 1 and (count_list[-1] == count_list[-2] + 1): # один отличается от остальных и его кол-во больше на 1 
        return True
    else: 
        return False