def TreeOfLife(H:int, W:int, N:int, tree:str):
    def init(tree):
        for i in range(len(tree)):
            tree[i] = list(tree[i])
            for j in range(len(tree[i])):
                if tree[i][j] == '.':
                    tree[i][j] = 0
                else:
                    tree[i][j] = 1
        return tree
    
    def chet(tree):  # Ветки стареют на 1 год
        for i in range(len(tree)):
            for j in range(len(tree[i])):
                tree[i][j] += 1
        return tree

    def nechet(tree):
        tree = chet(tree)

        tree_new = list(tree)  # Создать глубокую копию tree
        for i in range(len(tree)):
            tree_new[i] = list(tree[i])

        for i in range(len(tree)):  # Удалить старые ветки
            for j in range(len(tree[i])):
                if tree_new[i][j] != 0:
                    tree_new[i][j] = tree[i][j]
                if tree[i][j] >= 3:
                    tree_new[i][j] = 0
                    if j + 1 < len(tree[i]):
                        tree_new[i][j + 1] = 0
                    if j - 1 >= 0:
                        tree_new[i][j - 1] = 0
                    if i + 1 < len(tree):
                        tree_new[i + 1][j] = 0
                    if i - 1 >= 0:
                        tree_new[i - 1][j] = 0
        return tree_new

    tree_arr = init(tree)

    for i in range(N):
        if i % 2 == 0:
            tree_arr = chet(tree_arr)
        else:
            tree_arr = nechet(tree_arr)
    
    for i in range(len(tree_arr)):
        for j in range(len(tree_arr[i])):
            if tree_arr[i][j] == 0:
                tree_arr[i][j] = '.'
            else:
                tree_arr[i][j] = '+'
        tree_arr[i] = ''.join(tree_arr[i])

    return tree_arr