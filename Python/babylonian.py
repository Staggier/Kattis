def babylonian():
    t = int(input())

    for case in range(t):
        s = input()

        if ',' not in s:
            print(s)
            continue

        lst = s.split(',')
        i = s.count(',')

        result = 0
        for num in lst:
            result += (int(num) if num != '' else 0) * (60 ** i)
            i -= 1

        print(result)

    return

babylonian()

        
