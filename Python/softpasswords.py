def capSwitch(s):
    t = ""
    for c in s:
        ch = str(c)
        t += ch.lower() if ch.isupper() else ch.upper()
    return t

def softpasswords():
    s, p = input(), input()
    digits = "1234567890"
    
    return "Yes" if s == p or s == capSwitch(p) or (len(s) - len(p) == 1 and (s[0] in digits or s[-1] in digits)) else "No"
    
    
print(softpasswords())
