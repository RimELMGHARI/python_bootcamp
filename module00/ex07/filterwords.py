def filterWords(text, n):
    L=[]
    text=text.split()
    for i in range(len(text)):
        if len(text[i])>=n:
            L.append(text[i])
    
    return L
            
