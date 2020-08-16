def runlengthencodingrun():
    inp = input().split()
    
    result = ""
    if inp[0] == "E":
        last = inp[1][0]
        count = 0
        for c in inp[1]:
            if c != last:
                result += last + str(count)
                count = 0
            count += 1
            last = c
        result += last + str(count)
    else:
        for i in range(0, len(inp[1]), 2):
            result += str(inp[1][i]) * int(inp[1][i + 1])
    return result
    
print(runlengthencodingrun())
