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
try:
    output=open(args[2],"w")
except:
    print("open error")
    sys.exit(1)

dic={"a":0,"x":0,"c":0,"m":0}
for x in file:
    for y in x:
        try:
            dic[y]+=1
        except:
            pass
for x,y in dic.items():
    output.write("{} ha {} ko arimasita.\n".format(x,y))
file.close()
output.close()