import sys
try:
    output_file=open("output","w")
    input_file=open("input","r")
except:
    print("open error")
    sys.exit(1)
for x in input_file:
    for count,y in enumerate(x):
        if(count>0 and y=="#"):
            output_file.write("\n")
            break
        elif(y=="#"):
            break
        else:
            output_file.write(y)
output_file.close()
input_file.close()