def LineAnalysis(line:str):
    if len(line) % 2 == 0:
        n1 = n2 = len(line) // 2
    else:
        n1 = len(line) // 2
        n2 = len(line) // 2 + 1

    line1 = line[:n1]
    line2 = line[n2:]
    line2 = line2[::-1]
    if line1 == line2:
        return True
    else: 
        return False