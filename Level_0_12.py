def MassVote(N, Votes):
    try:
        assert type(N) is int and N >=1 and N == len(Votes)
        for i in range(len(Votes)):  
            assert type(Votes[i]) is int and Votes[i] >= 0 # Проверяем Элемент массива (целое, положительное) 

        def max(s):  # Возвращает номер наибольшего эл-та массива
            MAX = s[0]
            j = 0
            for i in range(1, len(s)):
                if MAX < s[i]:
                    MAX = s[i]
                    j = i
            return j

        def sum(s):
            SUM = 0
            for i in range(len(s)):
                SUM += s[i]
            return SUM

        j = max(Votes)
        for i in range(len(Votes)):
            if j != i and Votes[i] == Votes[j]:
                rez = 'no winner'
                return rez
        
        if Votes[j] * 100 / sum(Votes) > 50:
            rez = 'majority winner ' + str(j + 1)
        else:
            rez = 'minority winner ' + str(j + 1)

        return rez
    
    except AssertionError:
        pass