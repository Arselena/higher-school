def BalancedParentheses(N):
    def init(S):
        rez = []
        for i in S:
            rez.append('(' + i + ')')
            rez.append(i + '()')
            rez.append('()' + i)
        return list(set(rez))  # Возвращаем список уникальных значений

    S = ['()']
    for i in range(N-1):
        S = init(S)
    
    S = ' '.join(S)
    return S