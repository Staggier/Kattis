def plantingtrees():
    n = int(input())
    lst = [int(x) for x in input().split()]

    lst.sort()
    lst.reverse()

    result = lst[0] + 1
    for i in range(n):
        if result < lst[i] + i + 2:
            result = lst[i] + i + 2
            
    return result

print(plantingtrees())
    
