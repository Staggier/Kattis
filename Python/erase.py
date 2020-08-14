def erase():
    n = int(input())
    lst = ['0', '1']

    file   = input()
    result = input()
    
    for i in range (len(file)):
        if lst[(lst.index(file[i]) + n) % 2] != result[i]:
            return "Deletion failed"
    return "Deletion succeeded"

print(erase())
