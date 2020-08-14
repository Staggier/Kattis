def pauleigon():
    n, p, q = [int(x) for x in input().split()]

    t = p + q
    if t == 0:
        print("paul")
        return
    if t // n % 2 == 0:
        print("paul")
    else:
        print("opponent")

pauleigon()
