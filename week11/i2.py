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
for x in file:
    for y in x:
        if(y=="9"):
            output.write(" ")
        elif(y=="3"):
            output.write("*")
        elif(y=="\n"):
            output.write("\n")
        else:
            output.write("X")
file.close()
output.close()
