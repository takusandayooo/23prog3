class Kakudo():
    def __init__(self, d):
        self.d = d
    def __str__(self):
        return "kakudo ha {} do desu.".format(self.d)
    def __add__(self,e):
        if(0<=self.d+e.d and self.d+e.d<=360):
            return "kakudo ha {} do desu.".format(self.d+e.d)
        else:
            return "kakudo ha {} do desu.".format(self.d+e.d-(self.d+e.d)//360*360)
    def __sub__(self,e):
        if(0<=self.d-e.d and self.d-e.d<=360):
            return "kakudo ha {} do desu.".format(self.d-e.d)
        else:
            return "kakudo ha {} do desu.".format(self.d-e.d+(self.d+e.d)//360*360)

a = Kakudo(350)
b = Kakudo(30)
c = a + b
print(c)
d = b - a
print(d)
e = int(input())
e = Kakudo(e)
f = a + e
print(f)
