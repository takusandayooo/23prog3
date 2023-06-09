class Car():
    def __init__(self, name, ps, cc):
        self.name = name
        self.ps = ps
        self.cc = cc
    def __str__(self):
        return "{:12s}: {} PS, {} cc".format(self.name, self.ps, self.cc)
    def newver(self,ps,cc):
        return "{:12s}: {} PS, {} cc".format(self.name+"-II", ps,cc)
         

c = []
s1 = Car("Crown", 240, 3000)
c.append(s1)
s2 = Car("Corona", 220, 2000)
c.append(s2)
s3 = Car("Collora", 140, 1500)
c.append(s3)
s4 = s1.newver(250, 3200)
c.append(s4)
s5 = s2.newver(230, 2200)
c.append(s5)
s6 = s3.newver(150, 1600)
c.append(s6)
for i in c:
	print(i)