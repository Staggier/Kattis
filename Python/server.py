def server():
    n, t = [int(x) for x in input().split()]
    
    k, ans = 0, 0
    for num in [int(x) for x in input().split()]:
        if k + num > t:
            break
        k += num
        ans += 1
        
    return ans
    
print(server())
