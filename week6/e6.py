class Hairetsu:
    def __init__(self, a):
        self.array = a
    def print(self):
        print(self.array)
    def kakeru(self,a):
        for x in range(len(self.array)):
            self.array[x]*=a
    def tasu(self,a):
        for x in range(len(self.array)):
            self.array[x]+=a
a = Hairetsu([3, 4, 5])
a.print()
a.kakeru(2)
a.print()
a.kakeru(3)
a.print()
a.tasu(10)
a.print()
a.tasu(100)
a.print()
