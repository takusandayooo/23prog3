def tri(a):
    for x in range(a):
        for y in range(a-1-x):
            print(" ",end="")
        for z in range(x*2+1):
            print("*",end="")
        print()
n = int(input())
tri(n)
