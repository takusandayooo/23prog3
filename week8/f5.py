class Student:
    def __init__(self, last, first, num):
        self.last = last
        self.first = first
        self.num = num
        self.year = 99
        self.subj = "??"
    def print(self):
        print(self.year, end="")
        print(self.subj, end="")
        print(self.num, end=" ")
        print(self.last, end=" ")
        print(self.first)
class StudentJouhou19(Student):
    def __init__(self, last, first, num):
        super().__init__(last, first, num)
        self.subj="j5"
        self.year=19
class StudentJouhou20(StudentJouhou19):
    def __init__(self, last, first, num):
        super().__init__(last, first, num)
        self.year=20


x = Student("Example", "Example", 100)
x.print()

y = StudentJouhou19("Yamada", "Ryota", 101)
y.print()

z = StudentJouhou20("Yoshida", "Ichiro", 107)
z.print()
