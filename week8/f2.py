class Myarray:
    def __init__(self,lis):
        self.lis=list(lis)
    def add(self,num):
        self.lis.append(num)
    def mysortup(self):
        for i in range(len(self.lis)):
            for j in range(i+1,len(self.lis)):
                if(self.lis[i]>self.lis[j]):
                    t=self.lis[i]
                    self.lis[i]=self.lis[j]
                    self.lis[j]=t
    def __str__(self):
        return "<<{}>>".format(str(self.lis))
    def mysortdown(self):
        for i in range(len(self.lis)):
            for j in range(i+1,len(self.lis)):
                if(self.lis[i]<self.lis[j]):
                    t=self.lis[i]
                    self.lis[i]=self.lis[j]
                    self.lis[j]=t
    def __str__(self):
        a=str(self.lis)
        b=a[1:-1]
        return "<< {} >>".format(b)
a = Myarray([])
a.add(3)
a.add(2)
a.add(1)
a.add(5)
a.add(4)
print(a)
a.mysortup()
print(a)
b = Myarray([2, 7, 3, 8, 4, 1, 6])
x = int(input())
b.add(x)
b.mysortdown()
print(b)