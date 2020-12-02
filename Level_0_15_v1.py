def TankRush(H1, W1, S1, H2, W2, S2):
    
    # Вырезаем список H2 x W2 из S1
    def find(S1, St_start, St_end, Col_start, Col_end):
        S1_new = S1[St_start:St_end]
        for i1 in range(len(S1_new)):
            S1_new[i1] = S1_new[i1][Col_start:Col_end]
        return S1_new

    # Разбиваем строки на подстроки по пробелу
    S1 = S1.split()  
    S2 = S2.split()

    # Ищем подстроку S2[0] во всех строках карты S1
    flag = False
    for i1 in range((H1 - H2) + 1): # строки S1
        index_end = 0
        j1 = 0
        while j1 in range(W1): # стролбцы S1
            index_start = S1[i1].find(S2[0], j1) # ИСПРАВЛЕНО index_end на j1
            if index_start != -1:
                index_end = index_start + W2 # ИСПАВЛЕНО H2 на W2
                St_end = i1 + H2
                S1_new = find(S1, i1, St_end, index_start, index_end) 
                
                if S1_new == S2:
                    flag = True
                    break
            j1 += 1
            
    return flag

# print(TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98'))  # == True
# print(TankRush(3,3, '321 694 798', 2, 2, '69 98'))  # == False
# print(TankRush(3, 6, '343434 234980 000985', 2, 3, '343 498'))  # == True
# print(TankRush(5, 10, '122456789 548458632 456322486 231685222 576521354', 5, 2, '89 32 86 22 54'))  # == True
# print(TankRush(5, 10, '122456789 548458632 456322486 231685222 576521354', 4, 2, '54 45 23 57'))  # == True
# print(TankRush(5, 10, '122456789 548458632 456322486 231685222 576521354', 5, 10, '122456789 548458632 456322486 231685222 576521354'))  # == True

# 122456789   22 
# 548458632   54
# 456322486
# 231685222
# 576521354