def saidai(v):
    max=v[0]
    for x in v:
        if(max<x):
            max=x
    return max
def saishou(v):
    min=v[0]
    for x in v:
        if(min>x):
            min=x
    return min

x = int(input())
v = [1,  3,  7,  -1,  x, 9,  12,  4]
max = saidai(v)
min = saishou(v)
print("max is {}".format(max))
print("min is {}".format(min))
