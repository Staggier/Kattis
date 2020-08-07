def area():
    inp = [int(x) for x in input().split()]

    pol = []
    for i in range(1, (inp[0] * 2) + 1, 2):
        pol.append([inp[i], inp[i + 1]])
        
    pol.append([pol[0][0], pol[0][1]])
    half1, half2 = 0, 0
    val = inp[0]
    for i in range(val):
        if i != val:
            half1 += (pol[i][0] * pol[i + 1][1])
            half2 += (pol[i][1] * pol[i + 1][0])

    return abs(half1 - half2) / 2

def func():
    n = int(input())

    for i in range(n):
        print(area())

func()
