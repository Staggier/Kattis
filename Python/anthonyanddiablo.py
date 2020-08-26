import math

def anthonyanddiablo():
    a, c = map(float, input().split())
    
    r = c / (2 * math.pi)
    area = math.pi * (r ** 2)
    
    print("Diablo is happy!" if area >= a else "Need more materials!")
    return
    
anthonyanddiablo()
