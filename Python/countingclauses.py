def countingclauses():
    n, k = [int(x) for x in input().split()]
    if n >= 8:
        return "satisfactory"
    else:
        return "unsatisfactory"
        
print(countingclauses())
