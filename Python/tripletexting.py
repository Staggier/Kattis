from os import sys

def tripletexting():
    s = input()

    n, k = len(s) // 3, 0
    lst = []
    for i in range(0, 3):
        lst.append(s[k:k + n])
        k += n 

    for word in lst:
        if lst.count(word) >= 2:
            print(word)
            return

tripletexting()
