def thegrandadventure():
    n = int(input())

    for i in range(n):
        line = input()

        lst = []
        b = True
        
        for c in line:
            if c in "$|*":
                lst.insert(0, c)
            elif c in "tjb":
                if len(lst) == 0:
                    b = False
                    break
                elif c == 't' and lst[0] == '|':
                    del lst[0]
                elif c == 'j' and lst[0] == '*':
                    del lst[0]
                elif c == 'b' and lst[0] == '$':
                    del lst[0]
                else:
                    b = False
                    break
        if b and len(lst) == 0:
            print("YES")
        else:
            print("NO")
        
    return

thegrandadventure()
