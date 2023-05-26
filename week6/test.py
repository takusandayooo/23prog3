class a:
    def __init__(self):
        self.b="あいうえお"
        self.c="書きくけこ"

    def __str__(self):
        return self.b+" "+self.c
li=a()
print(li)