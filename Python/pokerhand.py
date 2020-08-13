from os import sys

def pokerhand():
    hand = sys.stdin.readline().split()

    d = {}
    ans = 0
    for card in hand:
        d[card[0]] = 1 if d.get(card[0]) is None else d[card[0]] + 1
        ans = d[card[0]] if d[card[0]] > ans else ans
    return ans

print(pokerhand())
