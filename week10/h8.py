import sys
args=sys.argv
if len(args)!=4:
    print("ERROR: hikisuu ga tarimasen")
    sys.exit(1)
else:
    try:
        file1=open(args[1],"r")
        file2=open(args[2],"r")
        file3=open(args[3],"a")
    except:
        print("open error")
        sys.exit(1)
for x in file1:
    file3.write(x)
    file3.write(file2.readline())
file1.close()
file2.close()
file3.close()


