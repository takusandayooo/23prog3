class Hako:
    def __init__(self, tate, yoko, takasa):
        self.tate = tate
        self.yoko = yoko
        self.takasa = takasa
    def taiseki(self):
        return self.tate*self.yoko*self.takasa
def taiseki(self):
    return self.tate*self.yoko*self.takasa

x = Hako(3, 4, 5)
print(x.taiseki())
print(taiseki(x))
y = Hako(1, 2, 3)
print(y.taiseki())
print(taiseki(y))

