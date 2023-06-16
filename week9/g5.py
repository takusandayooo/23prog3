class Students:
    def __init__(self, a):
        self.list = a
    def get_fm(self, t):
        a = []
        for i in self.list:
            if i.danjo == t:
                a.append(i)
        return a
    def get_gakka(self, t):
        a = []
        for i in self.list:
            if i.gakka == t:
                a.append(i)
        return a
    def get_gakkadanjo(self, s, t):
        a = [i for i in self.list if i.gakka==s and i.danjo==t]
        return a

class Student:
    def __init__(self, a, b, c, d, e):
        self.no = a
        self.shi = b
        self.mei = c
        self.danjo = d
        self.gakka = e
    def __str__(self):
        return "{} {} {} {} {}".format(
        self.no, self.shi, self.mei, self.danjo, self.gakka)
d = []
x = Student("96a001", "Oootsuka", "Akira", "M", "Jouhou")
d.append(x)
x = Student("96b002", "Satou", "Masaki", "M", "Jinbun")
d.append(x)
x = Student("97c001", "Sakuma", "Touko", "F", "Jouhou")
d.append(x)
x = Student("97d002", "Nakagomi", "Kouya", "M", "Keiei")
d.append(x)
x = Student("98e005", "Hattori", "Jyunko", "F", "Rikou")
d.append(x)
x = Student("98f001", "Ishida", "Yoshitaka", "M", "Jinbun")
d.append(x)
x = Student("98h002", "Ooki", "Syuuji", "M", "Keiei")
d.append(x)
x = Student("98s003", "Kitajima", "Kouji", "M", "Rikou")
d.append(x)
x = Student("98m004", "Yamada", "Minami", "F", "Jinbun")
d.append(x)
x = Student("98n006", "Yoshida", "Hiroko", "F", "Rikou")
d.append(x)

a = Students(d)
b = a.get_fm("F")
for i in b:
    print(i)
print("========")
c = a.get_gakka("Jouhou")
for i in c:
    print(i)
print("========")
d = a.get_gakkadanjo("Jinbun", "M")
for i in d:
    print(i)
