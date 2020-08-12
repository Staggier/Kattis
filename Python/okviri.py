def func():
    s = input()
    
    n  = len(s)
    i = 1
    c = 0
    
    result = ""
    for j in range(5):
        for k in range(n):
            ch = '*' if (k + 1) % 3 == 0 else '#'
            if j == 0 or j == 4:
                if (k + 1) == n:
                    result += ".." + ch + ".."
                else:
                    result += ".." + ch + "."
            elif j == 1 or j == 3:
                if (k + 1) == n:
                    result += "." + ch + "." + ch + "."
                else:
                    result += "." + ch + "." + ch 
            else:
                if (k + 1) == n:
                    if k != 0 and k % 3 == 0:
                        result += "*" + "." + s[k] + "." + ch
                    else:
                        result += ch + "." + s[k] + "." + ch
                elif k != 0 and k % 3 == 0:
                    result += "*" + "." + s[k] + "."
                else:
                    result += ch + "." + s[k] + "."
                
            i += 1
        result += "\n"
    print(result[:len(result) - 1])
    return
    
func()
