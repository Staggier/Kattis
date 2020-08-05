def apaxianparent():
    y, p = input().split()
    l = len(y) - 1
    print(y + p if y[l - 1:] == 'ex' else y + "x" + p if y[l] == 'e' else y[:l] + "ex" + p if y[l] in ['a', 'i', 'o', 'u'] else y + "ex" + p)
    return

apaxianparent()
    
