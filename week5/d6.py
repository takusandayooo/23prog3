def recprint(x, n) :
        if(n<len(x)-1):
                print(x[n],end=" ")
                recprint(x,n+1)
        else:
                print("")
def charprint(a) :
        for i in a :
                if (i != 'END') :
                        print(i, end=' ')
        print("")
        return
        
a=['a', 'i', 'u', 'e', 'o', 'END']
charprint(a)
recprint(a, 0)

b=[]
c='a'
while (c != 'END') :
        c = input()
        b = b + [c]
charprint(b)
recprint(b, 0)
