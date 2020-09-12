import sys

def func():
    n = int(input())
    
    for i in range(n):
        s = input().split()
        lst = []

        t = s
        while t[0] != "what":
            t = input().split()
            lst.append(t[2])

        result = ""
        for word in s:
            if word not in lst:
                result += " " + word

        print(result[1:])
        
    return

func()
