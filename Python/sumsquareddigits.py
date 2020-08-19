def base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
    
def func():
    n = int(input())
        
    for i in range(n):
        i, n, k = [int(x) for x in input().split()]
        lst = [int(x) for x in base(k, n)]
        print(i, sum(map((lambda num: num ** 2), lst)))
    return

func()
