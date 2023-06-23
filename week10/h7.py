import sys
def head(file,n):
    count=0
    for x in range(n):
        print(file.readline(),end="")
print("Input number", end = " ")
n = int(input())
try:
    ifx=open("xxx","r")
except:
    print("open error")
    sys.exit(1)
head(ifx, n)
ifx.close()
