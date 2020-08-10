def hiddenpassword():
    key, msg = input().split()

    key = list(key)
    c = 0

    lst = []
    for ch in msg:
        if ch in key:
            if ch == key[c]:
                c += 1
                if c == len(key):
                    return "PASS"
                lst.append(ch)
            else:
                if ch not in lst or lst.count(ch) != key.count(ch):
                    return "FAIL"
    if c == len(key):
        return "PASS"
    else:
        return "FAIL"

print(hiddenpassword())
