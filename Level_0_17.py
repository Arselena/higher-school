def LineAnalysis(line:str):
    if line == '' or line == '*' or line == '**' or line == '*.*' or line == '***':
        return True
    
    N = len(line)
    s = line[1:N-1].split('*') # Убираем крайние звездочки и разделяем на подстроки по '*'
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            flag = True
        else: flag = False
    return flag