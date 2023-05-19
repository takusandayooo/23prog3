def rep(a, b):
    y=a*b
    return y   
def rect(a, b, c):
    for x in range(c):
        for z in range(a):
            print(" ",end="") 
        s=rep("x",b)
        print(s)
sp=int(input())
len=int(input())
line=int(input())
rect(sp, len, line)
