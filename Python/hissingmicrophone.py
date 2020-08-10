from os import sys
import re

def hiss():
    print("hiss" if re.search('ss', sys.stdin.readline()) else "no hiss")
    return

hiss()
