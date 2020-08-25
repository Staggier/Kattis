import math
import sys

def sumDiv(n):
    result = 1
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result += i
            if (i != n // i):
                result += (n // i)
            
    return result
    
def almostperfect():
    inp = [int(x) for x in sys.stdin.readlines()]
    for num in inp:
        k = sumDiv(num)
        
        if k == num:
            print(num, "perfect")
        elif abs(k - num) <= 2:
            print(num, "almost perfect")
        else:
            print(num, "not perfect")
    return

almostperfect()
