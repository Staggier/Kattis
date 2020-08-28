def sortofsorting():
    while True:
        n = int(input())

        if n == 0:
            break

        lst = []

        c = 0
        for i in range(n):
            lst.append(input())

        for name in sorted(lst, key=lambda s: (s[:2])):
            print(name)
        print()

    return

sortofsorting()
