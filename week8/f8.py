class Chouhoukei:
    def __init__(self, a, b):
        self.tate=a
        self.yoko=b
    def menseki(self):
        return self.tate*self.yoko

class Chokuhoutai(Chouhoukei):
    def __init__(self, a, b,c):
        super().__init__(a, b)
        self.takasa=c
    def taiseki(self):
         return self.tate*self.yoko*self.takasa

a = Chouhoukei(3, 4)
print("menseki ha {} x {} = {}".format(a.tate, a.yoko, a.menseki()))
b = Chokuhoutai(5, 6, 7)
print("taiseki ha {} x {} x {} = {}".format(b.tate, b.yoko, b.takasa, b.taiseki()))
