import sys

def recount():
    d = {}
    lst = []

    for name in sys.stdin.readlines():
        if name == "...":
            break
        if d.get(name) is None:
            d[name] = 1
            lst.append(name)
        else:
            d[name] += 1

    result, val = "", 0
    b = True
    
    for name in lst:
        if d[name] > val:
            b = True
            result = name
            val = d[name]
        elif d[name] == val:
            b = False
    return result if b else "Runoff!"

print(recount())
