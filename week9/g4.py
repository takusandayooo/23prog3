class Db:
    def __init__(self, a, b, c):
        self.num = a
        self.name = b
        self.point = c
    def katen(self, p):
        self.point[0] += p
        self.point[1] += p
        self.point[2] += p
    def printdb(self):
        print(
        "{:3d} {} no eigo={:3d} kokugo={:3d} sugaku={:3d}"
        .format(self.num, self.name, self.point[0],
        self.point[1], self.point[2])
        )
    def samepoint(self,num,name):
        return Db(num,name,self.point.copy())

db = []
kokugo = 10
eigo = 10
sugaku = 50

x = Db(100, "Sakuma", [kokugo, eigo, sugaku])
db.append(x)
y = x.samepoint(101, "Yamada")
db.append(y)

db[0].printdb()
db[1].printdb()

print("=====")
x.katen(20)

db[0].printdb()
db[1].printdb()
