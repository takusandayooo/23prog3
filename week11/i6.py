import sys
args=sys.argv
if len(args)!=3:
    print("ERROR: hikisuu ga tarimasen")
    sys.exit(1)
try:
    file=open(args[1],"r")
except:
    print("open error")
    sys.exit(1)
sets=set()
dic={}
for x in args[2]:
    sets.add(x)
for x in sets:
    dic[x]=0

for x in file:
    for y in x:
        try:
            dic[y]+=1
        except:
            pass
for x,y in dic.items():
    print("{} ha {} ko arimasita.".format(x,y))
file.close()