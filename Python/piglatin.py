import sys

def func():
    
    for line in sys.stdin.readlines():
        for word in line.split():
            if word[0] in "aeiouy":
                print(''.join([word, "yay "]), end=""),
                continue
            else:
                tail = ""
                for c in word:
                    if c not in "aeiouy":
                        tail += c
                    else:
                        print(''.join([word[word.index(c):], tail, "ay "]), end=""),
                        break
        print()
func()
