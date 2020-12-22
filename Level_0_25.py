def TransformTransform(A:int, N:int):
    def S(A):
        B = []
        for i in range(len(A)):
            for j in range(len(A)-i):
                k = i + j
                a = A[j:(k+1)]
                if a != []:
                    a_max = max(a)
                    B.append(a_max)
        return B
    
    b = S(S(A))
    rez = False
    if sum(b) % 2 == 0:
        rez = True
    
    return rez