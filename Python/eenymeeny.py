def eenymeeny():
    rhyme = len(input().split())
    count = int(input())

    names, t1, t2 = [], [], []
    for i in range(count):
        names.append(input())

    i = 0
    turn = True
    
    while count != 1:
        if turn:
            t1.append(names[(i + rhyme - 1) % count])
        else:
            t2.append(names[(i + rhyme - 1) % count])

        turn = True if turn is False else False

        j = i
        i = names.index(names[(i + rhyme - 1) % count])
        
        del names[(j + rhyme - 1) % count]

        count -= 1
    if turn:
        t1.append(names[0])
    else:
        t2.append(names[0])

    print(len(t1))
    for name in t1:
        print(name)
    print(len(t2))
    for name in t2:
        print(name)
    return

eenymeeny()
        
