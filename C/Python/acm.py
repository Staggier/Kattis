from os import sys

def acm():
    time, count = 0, 0
    d = {}
    
    for line in sys.stdin:
        log = line.split()
        if log[0] == "-1":
            break
        if d.get(log[1]) is None:
            if log[2] == 'wrong':
                d[log[1]] = 20
            else:
                time += int(log[0])
                count += 1
        else:
            if log[2] == 'wrong':
                d[log[1]] += 20
            else:
                time += int(log[0]) + d[log[1]]
                count += 1
                
    print(count, time)
    return

acm()
