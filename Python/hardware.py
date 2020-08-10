import sys

def hardware():
    inp = sys.stdin.readlines()

    line = 1
    n = int(inp[0])
    
    for j in range(n):
        print(inp[line], inp[line + 1], sep="", end="")
        line += 2

        d = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
        lst = []
        while (line < len(inp) and (inp[line][0].isdigit() or inp[line][0] == '+')):
            lst.append(inp[line])
            line += 1

        for num in lst:
            if num[0] != '+':
                for c in num[:len(num) - 1]:
                    d[c] += 1
            else:
                s = num.split()
                for i in range(int(s[1]), int(s[2]) + 1, int(s[3])):
                    for c in str(i):
                        d[c] += 1
            
        r = 0
        for i in range(10):
            print("Make", d[str(i)[0]], "digit", i)
            r += d[str(i)[0]]
        print("In total", r, "digits" if r != 1 else "digit")

hardware()
