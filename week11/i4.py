class Yokoline:
    def __init__(self, a, b, c):
        self.sx = a
        self.sy = b
        self.lx = c
    def put(self, s, m):
        for i in range(self.lx):
            s[self.sx+i][self.sy] = m
class Tateline:
    def __init__(self, a, b, c):
        self.sx = a
        self.sy = b
        self.ly = c
    def put(self, s, m):
        for i in range(self.ly):
            s[self.sx][self.sy+i] = m

def display(s):
    for i in range(19, -1, -1):
        print("{:2d}  ".format(i), end="")
        for j in range(60):
            print(s[j][i], end="")
        print()
    print()
    print("    ", end="")
    for j in range(6):
        print("{}         ".format(j), end="")
    print()
    print("    ", end="")
    for j in range(6):
        print("0123456789", end="")
    print()
class Slant:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def put(self,s,f):
        if(self.c<0):
            for i in range(self.c*-1):
                s[self.a+i][self.b-i] = f
        else:
            for i in range(self.c):
                s[self.a+i][self.b+i] = f


s = []
for i in range(60):
    b = []
    for i in range(20):
        b.append(".")
    s.append(b)

a = Yokoline(2, 3, 8)
a.put(s, '#')
b = Tateline(2, 3, 8)
b.put(s, '#')

e = Slant(40, 4, 8)
e.put(s, '%')
f = Slant(20, 12, -8)
f.put(s, '%')

display(s)
