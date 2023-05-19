class Syugou:
    def __init__(self,x):
        self.sets=set()
        self.x=x
    def list2syugou(self):
        for x in self.x:
            self.sets.add(x)
        return self.sets
x = [1, 2, 2, 3, 5, 3, 4, 6, 2, 7]
s = Syugou(x).list2syugou()
print(s)
