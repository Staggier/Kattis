import sys

def addingwords():
    d = {}
    
    for line in sys.stdin.readlines():
        s = line.split()

        if s[0] == "def":
            t = int(s[2])
            if d.get(s[1]) is not None:
                del d[d[s[1]]]
            d[s[1]] = t
            d[t] = s[1]

        elif s[0] == "calc":
            eq = ""

            for word in s[1:]:
                if word not in "+-=" and d.get(word) is None:
                    break
                elif word in "+-=":
                    if word in "+-":
                        eq += " " + word + " "
                else:
                    eq += str(d[word])
                    
            try:
                num = eval(eq)
                ans = "unknown" if d.get(num) is None else d[num]
                print(' '.join(s[1:]), ans, sep=" ")
            except:
                print(' '.join(s[1:]), "unknown", sep=" ")
                
        else:
            d.clear()
            d = {}

addingwords()
