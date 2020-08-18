def karte():
    d = {'H':[], 'K':[], 'P':[], 'T':[]}
    
    s = input()
    i = 0
    
    while i < len(s) - 2:
        t = s[i + 1] + s[i + 2]
        if t in d[s[i]]:
            print("GRESKA")
            return
        else:
            d[s[i]].append(t)
        i += 3
        
    for suit in "PKHT":
        print(13 - len(d[suit]), end=" "), 
    return
    
karte()
