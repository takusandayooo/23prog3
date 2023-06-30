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

class Rectf:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def put(self,s,f):
        for i in range(self.c):
            for t in range(self.d):
                s[self.a+i][self.b+t] = f
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

d = Rectf(15, 7, 20, 11)
d.put(s, '*')

display(s)
