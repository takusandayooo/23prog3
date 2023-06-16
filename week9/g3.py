def finddata(lis,kensaku):
    liss=[]
    for count,x in enumerate(lis):
        liss=x.split()
        for y in liss:
            if(y==kensaku):
                print(lis[count])
                return 
        liss.clear()



db = []
db.append("Yamada	Toshiro  24j4788")
db.append ( "  24j5145    Yoshida	Toshi  ")
db.append ( "Yokoyama	26j5123  Toshiko  ")
db.append ( "Takao	T5j5195    Nishi	")
db.append ( "25j5192    Nishida	Yoshio  ")

finddata(db, "Toshi")
finddata(db, "Toshiko")
finddata(db, "Nishi")
