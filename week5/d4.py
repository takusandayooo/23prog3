class Select:
    def __init__(self,x):
        self.x=x
        
    def cut(self):
        lists=[]
        for y in self.x:
            if(y>=0):
                lists.append(y)
        return lists
x = [-1,  1,  2,  0,  -1,  5,  -2,  4,  0,  29]
y = Select(x).cut()
print(y)

