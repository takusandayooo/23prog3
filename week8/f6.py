class Car:
        def __init__(self, name, ps, cc):
                self.name = name
                self.ps = ps
                self.cc = cc
        def __str__(self):
                return "{}  no ps ha {} de cc ha {} desu.".format(self.name,self.ps,self.cc)
def sortbyps(p):
        for i in range(len(p)):
                for j in range(i+1,len(p)):
                        if(p[i].ps>p[j].ps):
                                t=p[i]
                                p[i]=p[j]
                                p[j]=t
def sortbycc(p):
        for i in range(len(p)):
                for j in range(i+1,len(p)):
                        if(p[i].cc>p[j].cc):
                                t=p[i]
                                p[i]=p[j]
                                p[j]=t


a = Car("crown", 240, 3000)
b = Car("color", 99, 999)
p = [a, b]
c = Car("celica", 280, 2000)
p.append(c)
d = Car("corona", 180, 2500)
p.append(d)

print("===============")
print("original")
print("===============")
for n in p:
        print(n)

print("===============")
print("sorted by ps(bariki)")
print("===============")
sortbyps(p)
for n in p:
        print(n)

print("===============")
print("sorted by cc(haikiryou)")
print("===============")
sortbycc(p)
for n in p:
        print(n)
