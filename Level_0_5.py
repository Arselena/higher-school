import numpy as np

def SynchronizingTables(N, ids, salary):
    try:
        assert type(N) is int and N >= 0  # Проверяем число N (целое, положительное)
        assert N == len(ids) == len(salary) 
        for i in range(len(ids)):  # Проверяем, что массив -- неповторяющиеся цифры
            for j in range(i+1, len(ids)):
                assert ids[i] != ids[j]
        for i in range(len(ids)):  
            assert type(ids[i]) is int and ids[i] >= 0 # Проверяем Элемент массива (целое, положительное) 
        for i in range(len(salary)):  
            assert type(salary[i]) is int and salary[i] >= 0 # Проверяем Элемент массива (целое, положительное)

        #Создаем многомерные массивы
        ids = np.array(ids)
        salary = np.array(salary)
        key = np.array(range(1,N+1))

        # Сортируем массивы
        key_ids = key[np.argsort(ids)]  # Массив key в порядке возрастания массива ids
        salary_sort = np.sort(salary)
        
        salary_ids = salary_sort[np.argsort(key_ids)]  # Массив salary_sort в порядке возрастания массива key

        #return np.array(salary_ids).tolist()  # Вывести рез-т в виде списка
        return np.array(salary_ids).tolist()

    except AssertionError: 
        pass # Ничего не делать