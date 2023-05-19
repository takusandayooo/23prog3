def rep(a, b):
    y=a*b
    return y
def printbar(n):
    for x in n:
        a=rep("#",x)
        print(a)

x = int(input())

a=[5, 1, 2]
printbar(a)
print("----------")

v=[3, 5, 9, 2, x]
printbar(v)
