import math
def primeFactors(n): 
    result = 0
    while n % 2 == 0:
        result += 1
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i == 0: 
            result += 1
            n = n / i
     
    return result + 1 if n > 2 else result
    
def listgame():
    n = int(input())
    print(primeFactors(n))
    return
    
listgame()
