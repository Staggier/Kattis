import sys

def most_frequent(lst): 
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in d:
        if lst.count(num) == 5:
            return num
    return -1

def timebomb():
    zero = ["***", "* *", "* *", "* *", "***"]
    one =  ["  *", "  *", "  *", "  *", "  *"]
    two =  ["***", "  *", "***", "*  ", "***"]
    three = ["***", "  *", "***", "  *", "***"]
    four = ["* *", "* *", "***", "  *", "  *"]
    five = ["***", "*  ", "***", "  *", "***"]
    six = ["***", "*  ", "***", "* *", "***"]
    seven = ["***", "  *", "  *", "  *", "  *"]
    eight = ["***", "* *", "***", "* *", "***"]
    nine = ["***", "* *", "***", "  *", "***"]

    
    inp = sys.stdin.readlines()
    i, j = 0, 0

    lst = [[] for x in range(0, len(inp[0]), 4)]
    num = [zero, one, two, three, four, five, six, seven, eight, nine]

    for line in inp:
        k = 0
        for j in range(0, len(line), 4):
            #print(line[j:j + 3])
            for n in num:
                if line[j:j + 3] == n[i]:
                    lst[k].append(num.index(n))
            k += 1
        i += 1

    result = 1

    for n in lst:
        result *= 10
        k = most_frequent(n)
        if k != -1:
            result += k
        else:
            result // 10

    return "BEER!!" if (result % (10 ** len(lst))) % 6 == 0 else "BOOM!!"
                    
        
print(timebomb())
