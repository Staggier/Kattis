def t9():
    d = {
            ' ':"0",
            'a':"2",
            'b':"22",
            'c':"222",
            'd':"3",
            'e':"33",
            'f':"333",
            'g':"4",
            'h':"44",
            'i':"444",
            'j':"5",
            'k':"55",
            'l':"555",
            'm':"6",
            'n':"66",
            'o':"666",
            'p':"7",
            'q':"77",
            'r':"777",
            's':"7777",
            't':"8",
            'u':"88",
            'v':"888",
            'w':"9",
            'x':"99",
            'y':"999",
            'z':"9999"
        }

    n = int(input())

    for i in range(n):
        last = ''
        print("Case #", i + 1, ":", sep="", end=" ")
        for c in input():
            if last != '':
                if d[last[0]][0] == d[c][0]:
                    print(" ", d[c], sep="", end="")
                else:
                    print(d[c], end="")
            else:
                print(d[c], end="")
            last = c
        print()
    return

t9()
