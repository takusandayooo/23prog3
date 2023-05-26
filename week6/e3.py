class Student:
    def __init__(self,a=00,b="xx",c=0,miyozi="Miyoji",namae="Namae"):
        self.a=a
        self.b=b
        self.c=c
        self.miyozi=miyozi
        self.namae=namae
    def __str__(self):
        return "{:0>2}{}{:0>3} {:12}{:10}".format(self.a,self.b,self.c,self.miyozi,self.namae )
a = Student()
x = Student(19, "j5", 1, "Aoki", "Taro")
y = Student(19, "j5", 11, "Ikeda", "Jiro")
z = Student(19, "j5", 123, "Uemura", "Saburo")

print(a)
print(x)
print(y)
print(z)
