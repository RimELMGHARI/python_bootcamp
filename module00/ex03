def text_analyzer(text):
    maj=mini=ponc=esp=0
    if text=="":
        return "text is empty."

    for char in text:
        if (65<=ord(char)<=90):
            maj+=1
        if (97<=ord(char)<=122):
            mini+=1
        if (33<=ord(char)<=47 or 58<=ord(char)<=63 ):
            ponc+=1
        if (ord(char)==32):
            esp+=1
        
    print("-", maj,"upper letters.")
    print("-", mini,"lower letters.")
    print("-", ponc,"ponctuaton marks.")
    print("-", esp,"spaces.")
