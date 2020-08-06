from os import sys

def busnumbers():
    n = int(sys.stdin.readline())

    lst = [int(x) for x in sys.stdin.readline().split()]
    lst.sort()
    lst.append(0)

    s = ""
    c, last = 1, lst[0]
    
    for num in lst[1:]:
        if num != last + 1:
            s += '-' + str(last) if c >= 3 else ' ' + str(last)
            c = 1
        else:
            s += ' ' + str(last) if c == 1 else ""
            c += 1
        last = num
                
    print(s[1:])
    return
            
busnumbers()
                
