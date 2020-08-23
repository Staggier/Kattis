def modsort(lst):
    b = False
    n = len(lst)
    
    while not b:
        b = True
        for j in range(n - 1):
            if lst[j][1] == lst[j + 1][1]:
                if lst[j][0] > lst[j + 1][0]:
                    t = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = t
                    b = False
    return lst

def warehouse():
    n = int(input())
    
    lst = []
    d = {}
    j = 0
    
    for i in range(n):
        s = input().split()
        if d.get(s[0]) is None:
            lst.append([s[0], int(s[1])])
            d[s[0]] = j
            j += 1
        else:
            lst[d[s[0]]][1] += int(s[1])
            
    lst = sorted(lst, key = lambda lst : lst[1], reverse=True)
    lst = modsort(lst)
    print(j)
    for item in lst:
        print(item[0], item[1])
     
def main():
    t = int(input())
    for i in range(t):
        warehouse()
        
main()
