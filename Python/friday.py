def friday():
    t = int(input())

    for i in range(t):
        d, m = [int(x) for x in input().split()]
        days = [int(x) for x in input().split()]

        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        c = 0

        f = 0
        for day in days:
            for j in range(day):
                if j == 12:
                    if week[c % 7] == "Friday":
                        f += 1
                    c += (day - 12)
                    break
                c += 1

        print(f)
    
friday()
