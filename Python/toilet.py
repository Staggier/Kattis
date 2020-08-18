def toiletseat():
    s = input()
    p1, p2, p3 = 0, 0, 0

    c = s[0]
    for i in range(1, len(s)):
        if c != s[i]:
            p1 += 1
            c = s[i]
        if c != 'U':
            p1 += 1
            c = 'U'

    c = s[0]
    for i in range(1, len(s)):
        if c != s[i]:
            p2 += 1
            c = s[i]
        if c != 'D':
            p2 += 1
            c = 'D'


    last = s[0]
    for i in range(1, len(s)):
        if s[i] != last:
            p3 += 1
        last = s[i]

    print(p1, p2, p3, sep="\n", end="")
    return

toiletseat()
