import sys
args=sys.argv
if len(args)!=2:
    print("ERROR: hikisuu ga tarimasen")
    sys.exit(1)
else:
    f=open(args[1],"r")
    for x in f:
        if(x[0]!="#"):
            print(x,end="")
    f.close()