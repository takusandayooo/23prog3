import sys
args=sys.argv
if len(args)!=3:
    print("ERROR: hikisuu ga tarimasen")
    sys.exit(1)
try:
    file1=open(args[1],"r")
except:
    print("open error")
    sys.exit(1)
try:
    file2=open(args[2],"r")
except:
    print("open error")
    sys.exit(1)
count=1

z=0
for fileine in file1:
    if(fileine==file2.readline()):
        count+=1
    else:
        if(file2.readline()!=""):
            count+=1
        print("line {} is different.".format(count))
        z+=1
        break
if z==0:
    print("aa and bb is same.")
file1.close()
file2.close()

