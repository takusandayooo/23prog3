import sys
class Tensuu:
    def __init__(self,lists):
        lis=lists.strip().split()
        if(len(lis)==2):
            self.number=lis[0]
            self.exam=int(lis[1])
        else:
            print("ERROR: strange data")
            sys.exit(1)
class People:
    def __init__(self,lists):
        lis=lists.strip().split()
        if(len(lis)==2):
            self.name=lis[0]
            self.number=int(lis[1])
        else:
            print("ERROR: strange data")
            sys.exit(1)
def Total(name,kokugo,eigo,suugaku):
    lis=[]
    for x in name:
        for y in kokugo:
            if(y.number==x.number):
                kokugos=y.exam
                break
        for z in eigo:
            if(z.number==x.number):
                eigos=z.exam
                break
        for t in suugaku:
            if(t.number==t.number):
                suugakus=t.exam
                break
        lis.append([x.name,x.number,kokugos,eigos,suugakus])
        
try:
    names=open("names","r")
except:
    print("open error")
    sys.exit(1)
try:
    eigo=open("eigo","r")
except:
    print("open error")
    sys.exit(1)
try:
    kokugo=open("kokugo","r")
except:
    print("open error")
    sys.exit(1)
try:
    suugaku=open("sugaku","r")
except:
    print("open error")
    sys.exit(1)
name_lis=[]
for x in names:
    a=People(x)
    name_lis.append(a)
kokugo_lis=[]
for x in kokugo:
    a=Tensuu(x)
    kokugo_lis.append(a)
suugaku_lis=[]
for x in suugaku:
    a=Tensuu(x)
    suugaku_lis.append(a)
eigo_lis=[]
for x in eigo:
    a=Tensuu(x)
    eigo_lis.append(a)
a=Total(name_lis,kokugo_lis,eigo_lis,suugaku_lis)

