def apaxiaaans():
    s = input()
    ans = str(s[0])

    b = True
    i = 1
    
    while i < len(s):
        last = s[i - 1]
        if s[i] == last:
            while i < len(s) and s[i] == last:
                i += 1
        else:
            ans += s[i]
            i += 1
        
    print(ans)

apaxiaaans()
