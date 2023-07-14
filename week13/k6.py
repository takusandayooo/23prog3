import sys

class Seiseki:
#####(A) class definition #####
    def __init__(self,lists):
        lis=lists.strip().split(",")
        if(lis[0][0]=="#"):
            self.number="#"
        else:
            if(len(lis)==6):
                self.number=lis[0]#学生番号
                self.first=lis[1]#名字
                self.last=lis[2]#名前
                self.attend=int(lis[3])#出席回数
                self.excer=int(lis[4])#通常得点
                self.exam=int(lis[5])#試験の得点
                self.total=self.excer+self.exam*4#総合得点
                if(self.attend<=10):
                    self.grade="F"
                else:
                    if(self.exam==-1):
                        self.grade="K"
                    else:
                        if(self.total<600):
                            self.grade="X"
                        else:
                            if(self.total<700):
                                self.grade="C"
                            else:
                                if(self.total<800):
                                    self.grade="B"
                                else:
                                    if(self.total<900):
                                       self.grade="A" 
                                    else:
                                        self.grade="S"
            else:
                print("ERROR: strange data")
                sys.exit(1)
#####(A) end #####
args = sys.argv
#####(B) arguments check  and file open ######
if len(args)!=2:
    print("ERROR: hikisuu ga tarimasen")
    sys.exit(1)
try:
    file=open(args[1],"r")
except:
    print("open error")
    sys.exit(1)
try:
    w=open("kekka","w")
except:
    print("open error")
    sys.exit(1)
#####(B) end #####

x=[]
#####(C) read data #####
for data in file:
    a=Seiseki(data)
    if(a.number!="#"):
        x.append(a)
#####(C) end #####
def sortbytotal(x):
    y=x.copy()
    for i in range(len(y)):
            for j in range(i+1,len(y)):
                    if(y[i].total>y[j].total):
                            t=y[i]
                            y[i]=y[j]
                            y[j]=t
    return y
    
y = sortbytotal(x)
for i in y:
    w.write("{} {:12} {:3} {}".format(i.number, i.first, i.total, i.grade))
    w.write("\n")
w.close()
file.close()
