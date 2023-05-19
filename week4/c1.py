def rect(a, b, c):
        for x in range(c):
            for z in range(a):
                print(" ",end="") 
            for y in range(b):
                print("*",end="")
            print(" ")
sp=int(input())
len=int(input())
line=int(input())
rect(sp, len, line)
