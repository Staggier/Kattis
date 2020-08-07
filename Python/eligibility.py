import math

def eligibility():
    n = int(input())

    for i in range(n):
        lst = input().split()

        studies = int(lst[1].split('/')[0])
        year = int(lst[2].split('/')[0])
        semesters = int(lst[3])

        
        if studies >= 2010:
            print(lst[0], "eligible")
        elif year >= 1991:
            print(lst[0], "eligible")
        elif math.ceil(semesters / 5) > 8:
            print(lst[0], "ineligible")
        else:
            print(lst[0], "coach petitions")
    return

eligibility()

        
        
