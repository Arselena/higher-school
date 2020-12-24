def BalancedParentheses(N):
    def hag(S): # найти и 'обнять' все правильные последовательности
        rez = []
        balance = 0
        for j in range(len(S)):  # возьмем одну строку
            pos = 0
            
            while pos < len(S[j])-1:  # перебираем все правильные последовательности от pos
                for i in range(pos, len(S[j])):  
                    if S[j][i] == '(':  
                        balance += 1
                    else:
                        balance -= 1
                    st_new = S[j][:i+1] + '()' + S[j][i+1:]  # везде вставляем ()
                    rez.append(st_new)
 
                    if balance == 0: # правильную последовательность 'обнимаем' ()
                        st = S[j][:pos] + '(' + S[j][pos:(i+1)] + ')' + S[j][i+1:]
                        rez.append(st)
                pos += 1
                while S[j][pos] != '(' and pos < len(S[j])-1:  # ищем открывающую скобку 
                    pos += 1
        return rez
    
    def init(S):  # итерация с одним вариантом
        rez = []
        for i in range(len(S)):
            # rez.append('(' + S[i] + ')')  # перекрывается hag
            # rez.append(S[i] + '()')
            # rez.append('()' + S[i])
            rez.extend(hag(S))
        return list(set(rez))  # Возвращаем список уникальных значений

    S = ['()']
    for i in range(N-1):
        S = init(S)
            
    print(len(S)) # == последовательности Каталана
    S = ' '.join(S)
    return S