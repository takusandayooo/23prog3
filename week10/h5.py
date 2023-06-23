class Database:
    def __init__(self,file):
        self.file=file
    def findno(self,no):
        f=open(self.file,"r")
        count=0
        for x in f:
            num=x.split()
            if(num[0]==no):
                print(x,end="")
                count=1
        f.close()
        if(count==0):
            print("{}: Sonna bangou no gakusei ha imasen".format(no))

    def findmyoji(self,myoji):
        f=open(self.file,"r")
        count=0
        for x in f:
            num=x.split()
            if(num[1]==myoji):
                print(x,end="")
                count=1
        f.close()
        if(count==0):
            print("{}: Sonna myoji no gakusei ha imasen".format(myoji))
    def findnamae(self,namae):
        f=open(self.file,"r")
        count=0
        for x in f:
            num=x.split()
            if(num[2]==namae):
                print(x,end="")
                count=1
        if(count==0):
            print("{}: Sonna namae no gakusei ha imasen".format(namae))
        f.close()
f = Database("students")

f.findmyoji("Aoki")
print()
f.findmyoji("Yamanouchi")
print()
f.findnamae("Atsushi")
print()
f.findnamae("Goemon")
print()
f.findno("21x5025")
print()
f.findno("99p9999")
