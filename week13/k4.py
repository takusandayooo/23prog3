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
def biggest(x):
    max=0
    max_num=0
    for num,i in enumerate(x):
        a=i.popu/i.dens
        if(a>max):
            max=a
            max_num=num
    return (x[max_num].name)    
def mostincr(x):
    max=0
    max_num=0
    for num,i in enumerate(x):
        a=i.incr
        if(num==0):
            max=a
        else:
            if(a>max):
                max=a
                max_num=num
    return (x[max_num].name)
def mostdecr(x):
    min=0
    min_num=0
    for num,i in enumerate(x):
        a=i.incr
        if(num==0):
            min=a
        else:
            if(a<min):
                min=a
                min_num=num
    return (x[min_num].name)
t = mostincr(x)
print("Most increased prefecture is {}".format(t))
t = mostdecr(x)
print("Most decreased prefecture is {}".format(t))
file.close()
file2.close()