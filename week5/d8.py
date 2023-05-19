class Kyu:
    def __init__(self,r):
        self.r=r
    def taiseki(self):
        return (4/3)*3.14*self.r**3
    def hyomenseki(self):
        return 4*3.14*self.r**2
hankei = float(input())
x = Kyu(hankei)
print("taiseki=", x.taiseki())
print("hyomenseki=", x.hyomenseki())
