class Student:
    def __init__(self, a, b, c):
        self.stno = a
        self.sei = b
        self.mei = c
    def printdata(self):
        print("{} {:10s} {:10s}".format(self.stno, self.sei, self.mei))
class JouhouStudent(Student):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.gakubu="Jouhou Gakka"
    def printdata(self):
        print("{} {:10s} {:10s} {}".format(self.stno, self.sei, self.mei,self.gakubu))
class KeieiStudent(Student):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.gakubu="Keiei Gakka"
    def printdata(self):
        print("{} {:10s} {:10s} {}".format(self.stno, self.sei, self.mei,self.gakubu))

x = Student("22h5900", "Yoshida",  "Taro")
x.printdata()

y = JouhouStudent("22j5900", "Tanaka", "Jiro")
y.printdata()

z = KeieiStudent("22s5765", "Kobayashi", "Saburo")
z.printdata()
