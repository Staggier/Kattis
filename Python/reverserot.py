def reverserot():
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
    while True:
        s = input().split()
        if s[0] == "0":
            break
            
        r = int(s[0])
        text = s[1][::-1]
        
        result = ""
        for c in text:
            result += alpha[(alpha.index(c) + r) % 28]
        print(result)
    return
        
reverserot()
