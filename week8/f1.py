def mysorted(a):
    lis=a.copy()
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if(lis[i]>lis[j]):
                t=lis[i]
                lis[i]=lis[j]
                lis[j]=t
    return lis

a = [3, 4, 2, 1, 5]
b = mysorted(a)
print(b)
print(a)
x = int(input())
y = int(input())
z = [3, 7, 2, 6, 1, x, y]
s = mysorted(z)
print(s)
