from statistics import median

def basicprogramming2():
    n, t = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    print(n, t, lst)

    if t == 1:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if lst[i] != lst[j] and lst[i] + lst[j] == 7777:
                    print("Yes")
                    return
        print("No")
        return
    elif t == 2:
        print("Unique" if n == len(list(set(lst))) else "Contains duplicate")
        return
    elif t == 3:
        k = n // 2
        for i in range(t):
            if lst.count(lst[i]) == k:
                print(lst[i])
                return
        print(-1)
        return
    elif t == 4:
        k = median(lst)
        print(k if n % 2 == 0 else str(k - 1) + " " + str(k + 1))
        return
    else:
        for num in sorted(lst):
            if num >= 100 and num <= 999:
                print(num, end=" ")
            elif num > 999:
                return

basicprogramming2()
            
