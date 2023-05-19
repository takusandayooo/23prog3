size1 = int(input())
size2 = int(input())
size3 = int(input())
class Box:
    def __init__(self,size):
        self.size1=size[0]
        self.size2=size[1]
        self.size3=size[2]
    def taiseki(self):
        return self.size1*self.size2*self.size3
    def hyomenseki(self):
        return self.size1*self.size2*2+self.size1*self.size3*2+self.size3*self.size2*2

x = Box([size1, size2, size3])
print("taiseki=", x.taiseki())
print("hyomenseki=", x.hyomenseki())
