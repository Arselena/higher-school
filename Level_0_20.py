S_current = ""  # Текущая строка
list_chang = []  # Список изменений
list_redo = []  # Список для отмены отмены
be_chang = False  # Признак, что были изменения

def BastShoe(command:str):
    global S_current, list_chang, list_redo, be_chang  # Помечаем глобальные переменные, что позволит записывать в них новые значения. Важно это сделать в начале ф-ии
    
    if command[0] == "1":  # Добавить строку
        if be_chang == True:  # Обнуляем список изменений и список отмены изменений
            list_chang = list_chang[-1:]
            list_redo = []
        S_current += command[2:]
        list_chang.append(S_current)
        be_chang = False  # Исправлено == на =

    elif command[0] == "2":  # Удалить n = int(command[2:]) символов
        if be_chang == True:  # Обнуляем список изменений и список отмены изменений
            list_chang = list_chang[-1:]
            list_redo = []
        i = len(S_current) - int(command[2:])
        if i > 0:
            S_current = S_current[:i]
        else: 
            S_current = ""
        list_chang.append(S_current)
        be_chang = False  # Исправлено == на =

    elif command[0] == "3":  # Выдать i-й символ текущей строки
        i = int(command[2:])
        if i <= (len(S_current) - 1):
            return S_current[i]
        else:
            return ""

    elif command[0] == "4":  # Отмена последней операции 1 или 2
        if len(list_chang) > 1:
            S_current = list_chang[-2]
            list_redo.append(list_chang[-1])
            list_chang.pop()  # Удаляем последний эл-т из списка
        else:
            S_current = list_chang[-1]
        be_chang = True

    elif command[0] == "5":  # выполнить заново последнюю отменённую операцию
        if len(list_redo) >= 1:
            S_current = list_redo[-1]
            list_chang.append(list_redo[-1])
            list_redo.pop()
        else:
            S_current = S_current
        be_chang = True
 
    return S_current