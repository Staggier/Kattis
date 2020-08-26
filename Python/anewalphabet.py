def anewalphabet():
    d = {
    'a':"@", 
    'b':"8", 
    'c':"(", 
    'd':"|)", 
    'e':"3", 
    'f':"#", 
    'g':"6", 
    'h':"[-]", 
    'i':"|", 
    'j':"_|", 
    'k':"|<", 
    'l':"1", 
    'm':"[]\/[]", 
    'n':"[]\[]", 
    'o':"0", 
    'p':"|D", 
    'q':"(,)", 
    'r':"|Z", 
    's':"$", 
    't':"\'][\'", 
    'u':"|_|", 
    'v':"\/", 
    'w':"\/\/", 
    'x':"}{", 
    'y':"`/", 
    'z':'2' 
    }
    
    for ch in input():
        c = ch.lower()
        print(c if d.get(c) is None else d[c], end="")
            
anewalphabet()
