def LineAnalysis(line:str):
    n = len(line)
    line = line[1:n-1]
    line = line.split('*')
    flag = True
    if len(line) >= 2:
        for i in range(len(line) - 1):
            if line[i] != line[i + 1]:
                flag = False
                break
    return flag