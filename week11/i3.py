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
class Rect:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def put(self,s,f):
        Yokoline(self.a,self.b,self.c).put(s,f)
        Tateline(self.a,self.b,self.d).put(s,f)
        Yokoline(self.a,self.b+self.d-1,self.c).put(s,f)
        Tateline(self.a+self.c-1,self.b,self.d).put(s,f)

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

c = Rect(5, 7, 5, 9)
c.put(s, '#')
d = Rect(15, 7, 20, 11)
d.put(s, '*')
display(s)
