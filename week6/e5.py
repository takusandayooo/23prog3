class Toyotacar:
	def __init__(self,name):
		self.name=name
		self.maker="Toyota"
class Nissancar:
	def __init__(self,name):
		self.name=name
		self.maker="Nissan"
a=Toyotacar("Collora")
b=Toyotacar("Crown")
c=Nissancar("Skyline")
d=Nissancar("Cedlic")
x=[a, b, c, d]
for i in x:
	print(i.name, end=" ")
	print("is make by", end=" ")
	print(i.maker)

