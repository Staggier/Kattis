import sys

def pervasiveheartmonitor():
    for line in sys.stdin.readlines():
        s = line.split()

        names = []
        numbers = []
        
        for word in s:
            if word.isalpha():
                names.append(word)
            else:
                numbers.append(float(word))
        print(sum(numbers)/len(numbers), ' '.join(names))

    return

pervasiveheartmonitor()
