def kemija():
    s, ans = input(), ""
    i = 0
    while i < len(s):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            ans += s[i]
            i += 3
        else:
            ans += s[i]
            i += 1
    print(ans)
    return

kemija()
            
