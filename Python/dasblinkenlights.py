def dasblinkenlights():
    p, q, s = [int(x) for x in input().split()]

    n = p if p < q else q
    t = n
    
    while t <= s:
        if t % p == 0 and t % q == 0:
            return "yes"
        t += n
    return "no"

print(dasblinkenlights())
