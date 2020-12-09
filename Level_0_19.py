def ShopOLAP(N:int, items:str):

    def sum(s_new):  # Складывает одинаковые позиции 
        i = 0
        while i in range(len(s_new) - 1):
            while s_new[i][0] == s_new[i+1][0]: 
                a = int(s_new[i][1]) + int(s_new[i + 1][1])
                s_new[i][1] = str(a)
                del s_new[i + 1]
                if i == len(s_new) - 1:
                    return s_new
            i += 1
        return s_new

    def sort_quantity(s): # Ключ для сортировки по кол-ву, кол-во преобразовать в int!
        return int(s[1])

    s_new = []
    for i in items: # Преобразовываем в список
        s_new.append(i.split())
    
    s_new.sort() # Сортируем по алфавиту
    s_new = sum(s_new) # Складываем одинаковые позиции 
    s_new.sort(key=sort_quantity, reverse=True) # Сортируем по кол-ву в порядке убывания
    
    s_new_str = []  # Преобразовываем в строку
    for i in s_new:
        i = ' '.join(i)
        s_new_str.append(i)
    
    return s_new_str