class Zukei():
    def __init__(self, d):
        self.d = d
        if len(d) > 3:
            print("Error in init: too big")
            quit()
    def what(self):
        if len(self.d) == 1:
            return "sen"
        elif len(self.d) == 2:
            return "Chouhoukei"
        elif len(self.d) == 3:
            return "Chokuhoutai"
        else :
            return "Miteigi"
    def printsize(self):
        if len(self.d) == 1:
            print("nagasa ha {} desu".format(self.d[0]))
        elif len(self.d) == 2:
            t = self.d[0] * self.d[1]
            print("menseki ha {} desu".format(t))
        elif len(self.d) == 3:
            t = self.d[0] * self.d[1] * self.d[2]
            print("taiseki ha {} desu".format(t))
        else :
            return "Unknwon"
    def __mul__(self,e):
        if(len(self.d)!=len(e.d)):
           print("Error: not defined")
        elif(len(self.d)==2 and len(e.d)==2):
            lis=checkar(self.d,e.d)
            return Zukei(lis)
        else:
            return Zukei([self.d[0],e.d[0]])
    
        
def checkar(a, b):
    if a[0] == b[0] or a[1] == b[0]:
        c = [a[0], a[1], b[1]]
    elif a[0] == b[1] or a[1] == b[1]:
        c = [a[0], a[1], b[0]]
    else:
        print("array error")
        quit()
    return c



a = Zukei([3])
print("a ha", a.what(), "desu")
a.printsize()
print("===========")
b = Zukei([3, 4])
print("b ha", b.what(), "desu")
b.printsize()
print("===========")
x = Zukei([3])
y = Zukei([5])
z = x * y
print("z ha", z.what(), "desu")
z.printsize()
print("===========")
p = Zukei([3, 4])
q = Zukei([4, 5])
r = p * q
print("r ha", r.what(), "desu")
r.printsize()
print("===========")
a * b
