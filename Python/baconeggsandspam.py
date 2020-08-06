def func():
    while True:
        n = int(input())
        if n == 0:
            break

        d = {}
        menu = []

        for i in range(n):
            lst = input().split()
            for item in lst[1:]:
                if d.get(item) is None:
                    d[item] = []
                    menu.append(item)
                d[item].append(lst[0])

        menu.sort()
        for item in menu:
            print(item, end=" "),

            for name in sorted(d[item]):
                print(name, end=" "),
            print()
        print()

    return

func()
