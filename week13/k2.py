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
#####(D) function difinition #####
def biggest(x):
    max=0
    max_num=0
    for num,i in enumerate(x):
        a=i.popu/i.dens
        if(num==0):
            max=a
        else:
            if(a>max):
                max=a
                max_num=num
    return (x[max_num].name)    

def mostdense(x):
    max=0
    max_num=0
    for num,i in enumerate(x):
        if(num==0):
            max=i.dens
        else:
            if(i.dens>max):
                max=i.dens
                max_num=num
    return (x[max_num].name)

#####(D) end #####
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


t = biggest(x)
print("Biggest prefecture is {}".format(t))
t = mostdense(x)
print("Most crowded prerecture is {}".format(t))

file.close()