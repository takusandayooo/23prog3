def recprintrev(x, n) :
        if(n>=0):
                print(x[n],end=" ")
                recprintrev(x,n-1)
        else:
                print("")

def charprint(a) :
        for i in range(len(a)-1, -1, -1) :
                print(a[i], end=' ')
        print("")
        return

a=['a', 'i', 'u', 'e', 'o']
charprint(a)
recprintrev(a, len(a)-1)

b=[]
c = input()
while (c != 'END') :
        b = b + [c]
        c = input()
charprint(b)
recprintrev(b, len(b)-1)
