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

        # Быстрая сортировка массива и упорядочивания key
        def partition(array, key, begin, end):
            pivot = begin
            for i in range(begin+1, end+1):
                if array[i] <= array[begin]:
                    pivot += 1
                    array[i], array[pivot] = array[pivot], array[i]
                    if key != []:
                        key[i], key[pivot] = key[pivot], key[i]
            array[pivot], array[begin] = array[begin], array[pivot]
            if key != []:
                key[pivot], key[begin] = key[begin], key[pivot]
            return pivot
            
        def quick_sort(array, key, begin=0, end=None):
            if end is None:
                end = len(array) - 1
            
            def _quicksort(array, key, begin, end):
                if begin >= end:
                    return
                pivot = partition(array, key, begin, end)
                _quicksort(array, key, begin, pivot-1)
                _quicksort(array, key, pivot+1, end)
            return _quicksort(array, key, begin, end)

        key = [i for i in range(1, N + 1)]        
        quick_sort(ids, key)
        quick_sort(salary, [])
        quick_sort(key, salary)
        return salary
    
    except AssertionError: 
        pass # Ничего не делать