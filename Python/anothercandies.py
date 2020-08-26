def anothercandies(): 
    t = int(input()) 
    for i in range(t):
        input()
        c, s = int(int(input())), 0 
        for i in range(c):
            s += int(input())
        print("YES" if s % c == 0 else "NO")
       
anothercandies()
