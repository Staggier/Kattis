def tornbygge():
    ans = 1

    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n - 1):
        if lst[i] < lst[i + 1]:
            ans += 1

    return ans

print(tornbygge())
