from os import sys

def is_spookmas():
    inp = sys.stdin.readline().split()
    if (inp[0] == 'DEC' and inp[1] == '25') or (inp[0] == 'OCT' and inp[1] == '31'):
        print('yup')
    else:
        print('nope')
    return

is_spookmas()
