def printtatebar(a):
    b=sorted(a)
    max=b[-1]
    for x in range(max,0,-1):
        for y in a:
            if(x<=y):
                print("#",end="")
            else:
                print(" ",end="")
        print()



x = int(input())
				
a=[5, 1, 2]
printtatebar(a)
print("----------")

v=[3, 5, 9, 2, x]
printtatebar(v)
