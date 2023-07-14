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

#####(E) function definition #####
def register(lis,a):
    for x in a:
        if(lis[0]==x.name):
            x.incr=int(lis[1])-int(lis[2])
            break
#####(E) end #####

args = sys.argv
#####(F) arguments check  and file open ######
if len(args)!=3:
    print("ERROR: hikisuu ga tarimasen")
    sys.exit(1)
try:
    file=open(args[1],"r")
except:
    print("open error")
    sys.exit(1)
try:
    file2=open(args[2],"r")
except:
    print("open error")
    sys.exit(1)
######(F) end #####

x=[]
#####(C) read data #####
for data in file:
    a=Pref(data)
    if(a.name!="#"):
        x.append(a)
#####(C) end #####


#####(G) read data from second file #####
for data in file2:
        lis=data.strip().split(",")
        if(lis[0][0]=="#"):
            pass
        else:   
            if(len(lis)==3):
                register(lis,x)
            else:
                print("ERROR: strange data")
                sys.exit(1)

#####(G) end #####

for i in x:
    print("{:12}".format(i.name), end="")
    print("{:10}".format(i.popu), end="")
    print("{:10}".format(i.incr))
file.close()
file2.close()
