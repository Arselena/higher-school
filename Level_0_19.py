def ShopOLAP(N:int, items:str):

    def sort_quantity(s): # Сортировка по кол-ву
        return s[1]

    s_new = []
    for i in items: # Преобразовываем в список
        s_new.append(i.split())
    
    s_new.sort() # Сортируем по алфавиту
    s_new.sort(key=sort_quantity, reverse=True) # Сортируем по кол-ву в порядке убывания
    
    s_new_str = []  # Преобразовываем в строку
    for i in s_new:
        i = ' '.join(i)
        s_new_str.append(i)
    
    return s_new_str