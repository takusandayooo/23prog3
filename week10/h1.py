import sys
args=sys.argv
if len(args)!=2:
    print("ERROR: hikisuu ga tarimasen")
    sys.exit(1)
else:
    f=open(args[1],"r")
    for count,x in enumerate(f):
        if(x!="\n"):
            print("{:6}  {}".format(count+1,x),end="")
    f.close()
