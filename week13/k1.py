import sys
#####(A) class definition #####
class Pref:
    def __init__(self,lists):
        lis=lists.strip().split(",")
        if(lis[0][0]=="#"):
            self.name="#"
        else:   
            if(len(lis)==3):
                self.name=lis[0]
                self.popu=int(lis[1])
                self.dens=float(lis[1])/float(lis[2])
            else:
                print("ERROR: strange data")
                sys.exit(1)
#####(A) end #####

#####(B) arguments check  and file open ######
args=sys.argv
if len(args)!=2:
    print("ERROR: hikisuu ga tarimasen")
    sys.exit(1)
try:
    file=open(args[1],"r")
except:
    print("open error")
    sys.exit(1)
#####(B) end #####

x=[]
#####(C) read data #####
for data in file:
    a=Pref(data)
    if(a.name!="#"):
        x.append(a)
#####(C) end #####

for i in x:
    print("{:12}".format(i.name), end="")
    print("{:10}".format(i.popu), end="")
    print("{:10.3f}".format(i.dens))

file.close()