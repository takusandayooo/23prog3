class Student:
    def __init__(self,a,b,c,miyozi,namae):
        self.a=a
        self.b=b
        self.c=c
        self.miyozi=miyozi
        self.namae=namae
    def print(self):
        print("{:0>2}{}{:0>3} {:12}{:10}".format(self.a,self.b,self.c,self.miyozi,self.namae))   
x = Student(19, "j5", 1, "Aoki", "Taro")
y = Student(19, "j5", 11, "Ikeda", "Jiro")
z = Student(19, "j5", 123, "Uemura", "Saburo")

x.print()
y.print()
z.print()

