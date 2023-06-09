class Database:
    def __init__(self, ar):
        self.ar = ar
    def add(self, x):
        self.ar.append(x)
class Student:
    def __init__(self, num, myoji, namae):
        self.num = num
        self.myoji = myoji
        self.namae = namae
    def print(self):
        print("{} {:10s} {:10s}".format(self.num, self.myoji, self.namae))
def findmyoji(a,b):
    lis=[]
    coun=0
    for x in range(len(a.ar)):
        if(a.ar[x].myoji==b):
            lis.append(x)
            coun=1
    if(coun==0):
        print( "ERROR: no such student {}".format(b))
    else:
        for x in lis:
            print("{} {:11s}{:11s}".format(a.ar[x].num,a.ar[x].myoji,a.ar[x].namae))
def findnamae(a,b):
    lis=[]
    coun=0
    for x in range(len(a.ar)):
        if(a.ar[x].namae==b):
            lis.append(x)
            coun=1
    if(coun==0):
        print( "ERROR: no such student {}".format(b))
    else:
        for x in lis:
            print("{} {:11s}{:11s}".format(a.ar[x].num,a.ar[x].myoji,a.ar[x].namae))
def findnum(a,b):
    lis=[]
    coun=0
    for x in range(len(a.ar)):
        if(a.ar[x].num==b):
            lis.append(x)
            coun=1
    if(coun==0):
        print( "ERROR: no such student {}".format(b))
    else:
        for x in lis:
            print("{} {:11s}{:11s}".format(a.ar[x].num,a.ar[x].myoji,a.ar[x].namae))
db = Database([])
f = Student("21x5001", "Aizawa", "Yuto")
db.add(f)
f = Student("21x5002", "Aoto", "Taro")
db.add(f)
f = Student("21x5003", "Aoyama", "Toshiro")
db.add(f)
f = Student("21x5004", "Ishida", "Yuji")
db.add(f)
f = Student("21x5005", "Yamada", "Youko")
db.add(f)
f = Student("21x5006", "Yamada", "Saburo")
db.add(f)
f = Student("21x5007", "Wada", "Taro")
db.add(f)

print("====================")
for i in db.ar:
    i.print()
print("====================")
print("====================")
findmyoji(db, "Aoto")
print("====================")
findmyoji(db, "Hoge")
print("====================")
findnamae(db, "Taro")
print("====================")
findnamae(db, "Shirou")
print("====================")
findnum(db, "21x5004")
print("====================")
findnum(db, "21x5100")
print("====================")
