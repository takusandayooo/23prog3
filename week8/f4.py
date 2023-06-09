class Sesshikashi:
    def __init__(self, a, b, c):
        self.start = a
        self.end = b
        self.step = c
    def printtable(self):
        for x in range (self.start, self.end, self.step):
            print("|{:6d} |{:12f} |".format( x, x*1.8+32))
class SesshikashiR(Sesshikashi):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    def printtable(slef):
        print ("+-------+-------------+\n| Sesshi| Kashi       |\n+-------+-------------+")
        super().printtable()
        print("+-------+-------------+")


x=Sesshikashi(0, 101, 5)
x.printtable()
print("")
print("")
x=SesshikashiR(0, 101, 5)
x.printtable()
