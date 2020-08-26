import sys

def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
        
    return result
    
def anagramcounting():
    for s in sys.stdin.readlines():
        f = factorial(len(s) - 1)
        k = 1
        
        lst = []
        for c in s:
            if c not in lst:
                lst.append(c)
                k *= factorial(s.count(c))
        print(f // k)
    
anagramcounting()
        
