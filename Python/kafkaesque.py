def func():
    n = int(input())

    lst = []
    for i in range(n):
        lst.append(int(input()))

    i = 0
    result = 0
    
    while len(lst) != 0:
        j = 0

        t = lst[0]
        while j < len(lst):
            if lst[j] >= t:
                t = lst[j]
                del lst[j]
                j -= 1
            else: break
                
            j += 1
        result += 1
    return result

print(func())
