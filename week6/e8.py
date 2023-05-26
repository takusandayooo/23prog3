class Data:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.goukei = score.sugaku+score.eigo+score.kokugo
class Score:
    def __init__(self, sugaku, eigo, kokugo):
        self.sugaku = sugaku
        self.eigo = eigo
        self.kokugo = kokugo
def grade(self):
    if(270<=self.goukei):
        return "S"
    elif(240<=self.goukei):
        return "A"
    elif (210<=self.goukei):
        return "B"
    elif(180<=self.goukei):
        return "C"
    else:
        return "X"
# Main start
Data.grade=grade
#
a = Score(20, 30, 40)
ma = Data("Yamada", a)
g = ma.grade()
print("Grade for {} is {}".format(ma.name, g))
#
b = Score(70, 90, 80)
mb = Data("Yoshida", b)
g = mb.grade()
print("Grade for {} is {}".format(mb.name, g))
#
c = Score(60, 60, 70)
mc = Data("Okada", c)
g = mc.grade()
print("Grade for {} is {}".format(mc.name, g))
