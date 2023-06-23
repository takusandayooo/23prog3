class File:
    def __init__(self,file):
        self.file=file
    def cat(self):
        f=open(self.file,"r")
        for x in f:
            print(x,end="")
        f.close()
    def copy(self,copy_file):
        f=open(self.file,"r")
        f2=open(copy_file,"w")
        for x in f:
            f2.write(x)
        f.close()
        f2.close()


f = File("file1")
print("==============")
print("file1 no naiyou desu.")
f.cat()
print("==============")
print("file1 wo file2 ni copy simasu.")
f.copy("file2")
